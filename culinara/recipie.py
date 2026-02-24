
import json

class Recipie:
    def __init__(self,file):
        with open(file,"r") as f:
            self.recipies = json.load(f)
    def get_recipies(self):
        result = []
        for recipe in self.recipies:
            result.append(recipe["name"])
        return result

    def get_recipe_data(self,name):
        for recipie in self.recipies:
            if recipie["name"].lower() == name.lower():
                result = ""
                result += f"        {recipie["name"].title()}\n"
                result += f"  Ingredients : Quantity\n"
                ingredients = recipie["ingredients"]
                for key in ingredients.keys():
                    result += f"  {str(key)} : {ingredients[key]}\n"
                return result
        return f"Not Found any recipe with name : {name.title()}" 
    
    def get_recipie(self,name):
        for recipie in self.recipies:
            if recipie["name"].lower() == name.lower():
                return recipie
        return None