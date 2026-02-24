
import json,shlex
class Pantry:
    def __init__(self,file,report_file):
        with open(file,"r") as f:
            self.pantry = json.load(f)
        self.file = file
        self.report_file = report_file
        with open(self.report_file,"r"):
            pass

    def update(self,item,qunatity):
        q = self.get_quantity(item)
        if (qunatity < 0):
            if q is None:
                print(f"Item {item}does not exist cannot use it." \
                "\nPlease add it to Inventory First.")
                return
            self.pantry[item] -= qunatity
        else:
            if q is None:
                self.pantry[item] = qunatity
                
            else:
                self.pantry[item] += qunatity
                
        with open(self.file,"w") as f:
            f.write(json.dumps(self.pantry))




    def get_quantity(self,name):
        for key in self.pantry.keys():
            if str(key).lower() == name.lower():
                return self.pantry[key]  
        return None

    def use_ingredient(self,item,quantity):
        q = self.get_quantity(item)
        if q is None:
            print(f"Item {item} does not exist cannot use it." \
            "\nPlease add it to Inventory First.")
            return
        
        if q < quantity:
            print(f"Error : insuficient Amount.Can't use {item}")
            return
        
        self.pantry[item] = self.pantry[item] - quantity
        with open(self.file,"w") as f:
            f.write(json.dumps(self.pantry))
        print(f"successfully used the item {item}")

            
    def process(self,file_path):
        report = open(self.report_file,"w")
        with open(file_path,"r") as f:
            for line in f.readlines():
                try:
                    command = shlex.split(line)
                    match(command[0].lower()):
                        case "add":
                            quantity = int(command[2])
                            self.update(command[1],quantity)
                            report.write(f"SUCCESS: {line}")
                        case "use":
                            quantity = int(command[2])
                            if quantity < 0:
                                quantity = -quantity
                            report.write(f"SUCCESS: {line}")
                        case _:
                            report.write(f"ERROR: Unknown Command \"{command[0]}\"")
                except ValueError:
                    report.write(f"ERROR(invalid Number): {line}")
                except:
                    report.write(f"ERROR(invalid Command): {line}")
                
        with open(self.file,"w") as f:
            f.write(json.dumps(self.pantry))
        print("Successfully processed the File.\n" \
                "A report file 'report\\report_file' is generated")

    def exit(self):
        with open(self.file,"w") as f:
            f.write(json.dumps(self.pantry))
                