from culinara.recipie import Recipie
from culinara.pantry import Pantry
import shlex

class CuinaraManager:
    def __init__(self,paths):
        self.recipie = Recipie(paths["recipe_file"])
        self.panrty = Pantry(paths["pantry_file"],paths["report_file"])
        self.report = paths["report_file"]
    def plan_mod(self,command):
        try:
            print("-----------------------------------\n")
            print("Welcome to the plan mode.")
            
            if len(command)  <= 2:
                print("Invalid Command.")
                print("\n-----------------------------------\n")
                return
            command = command[2:]
            cmd = command[0]
            match(cmd.lower()):
                case "recipe":
                    self.recipe_mode(command)
                case "pantry":
                    self.pantry_mode(command)
                case "exit":
                    print("Exiting now.")
                    self.panrty.exit()
                case "plan":
                    self.plan_command()
                case _:
                    print("Invalid Command. Try again.")
            
        except IndexError:
            print("Insificient Arguments provided.")
        except ValueError:
            print("Invalid command Provided")
        except:
            print("Bad Command.")
        print("-----------------------------------\n")

    def manage_mod(self):
        print("-----------------------------------\n")
        print("Welcome to the InterActive mode.")
        print("-----------------------------------\n")
        command = input(">")
        while True:
            command = shlex.split(command)
            while (len(command) == 0):
                command = input(">")
                command = shlex.split(command)
            cmd = command[0]
            print("-----------------------------------\n")
            match(cmd.lower()):
                case "recipe":
                    self.recipe_mode(command)
                case "pantry":
                    self.pantry_mode(command)
                case "plan":
                    self.plan_command()
                case "exit":
                    print("Exiting now.")
                    self.panrty.exit()
                    break
                case _:
                    print("Invalid Command. Try again.")
            print("-----------------------------------\n")
            command = input(">")

        print("Good bye Have a nice day.")

    def recipe_mode(self,commands):
        if len(commands) < 2:
            print("Invalid Command. Try Again")
            return
        report = open(self.report,"a")
        try:
            cmd = commands[1]
            match(cmd.lower()):
                case  "list":
                    recipies = self.recipie.get_recipies()
                    for i in range(len(recipies)):
                        print(f"{i+1}. {recipies[i]}")
                    report.write("Listed the Recipies.\n")
                case "view":
                    print(self.recipie.get_recipe_data(commands[2]))
                    report.write(f"Viewed recipe {commands[2]}\n")
                case "gap":
                    recipie = self.recipie.get_recipie(commands[2])
                    if recipie is None:
                        print(f"Not Found any recipe with name : {commands[2].title()}")
                        return

                    to_shop = []
                    ingredients = recipie["ingredients"]
                    for key in ingredients.keys():
                        q = self.panrty.get_quantity(str(key))
                        if q is None or q < ingredients[key]:
                            to_shop.append(str(key))
                    report.write(f"Performed Gap Analysis for recipie  {commands[2]}\n")
                    if len(to_shop) != 0:
                        print(f"Here is the Shooping List for the Recipe {commands[2]}:")
                        for i in range(len(to_shop)):
                            print(f"{i+1}. {to_shop[i]}")   
                    else:
                        print(f"Nothing is Missing for the {commands[2]} Recipie.")     
                case "cook":
                    report.write(f"started Cooking the Recipie {commands[2]}: \n\n")
                    check = self.is_cookable(commands[2])
                    if check is None:
                        report.write(f"\nOOPS! Cannot find a reciipie {commands[2]}\n")
                        return
                    if not check:
                        print("Error : Some Ingredients are not in required quantity.\nPlease Run Gap to see the Items Missing.")
                        report.write("\n\nOOPS! cannot cook some ingredients are missing.\n")
                        return
                    print(f"Successfully Cooked the {commands[2]}.")
                    report.write(f"\nSuccessfully Cooked the {commands[2]}.\n")
                case _:
                    print("Invalid Command. Try again.")
        except IndexError:
            print("Commands does not contains required Number of arguments")
        except ValueError:
            print("Invalid Number value in the command")
        except  FileNotFoundError:
            print("Invalid File Path is given.")
        except:
            print("An Error occurred. Please Try again.")
        finally:
            report.close()


    def is_cookable(self,name,cook=True):
        recipie = self.recipie.get_recipie(name)
        if recipie is None:
            print(f"Error: Not Found any recipe with name : {name.title()}")
            return None        
        ingredients = recipie["ingredients"]
        for key in ingredients.keys():
            q = self.panrty.get_quantity(str(key))
            if q is None or q < ingredients[key]:
                return False
            
        if cook:
            for key in ingredients.keys():
                self.panrty.update(str(key),-ingredients[key])
        return True
    

    def pantry_mode(self,commands):
        if len(commands) < 2:
            print("Invalid Command. Try Again")
            return
        
        try:
            cmd = commands[1]
            match(cmd.lower()):
                case "add":
                    quantity = int(commands[3])
                    if (quantity < 0):
                        print("Cant add Negative Amount.\nPlease use ingredient to do so.")
                        return
                    
                    self.panrty.update(commands[2],quantity)
                    print(f"successfuly added the {quantity} of {commands[2]}")
                case "use":
                    quantity = int(commands[3])
                    self.panrty.use_ingredient(commands[2],quantity)
                case "process":
                    self.panrty.process(commands[2])
                case _:
                    print("Invalid Command. Try again.")
        except IndexError:
            print("Commands does not contains required Number of arguments")
        except ValueError:
            print("Invalid Number value in the command")
        except  FileNotFoundError:
            print("Invalid File Path is given.")
        except :
            print("An Error occurred. Please Try again.")
             
    def plan_command(self):
        recipies = self.recipie.get_recipies()
        result = []
        for recipie in recipies:
            if(self.is_cookable(name=recipie,cook=False)):
                result.append(recipie)
        if len(result) == 0:
            print("No recipie is Cookable")
            return
        print("Following are the Cookable recipes:  ")
        for i in range(len(result)):
            print(f"{i+1}. {result[i]}")