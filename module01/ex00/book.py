from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if type(name) != str or len(name) == 0:
            raise ValueError("error: book name must be a none empty string")
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        recipe_type = ['starter', 'lunch', 'dessert']
        for t in recipe_type:
            for recipe in self.recipes_list[t]:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print('Recipe not found')
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        types = ['starter', 'lunch', 'dessert']
        if recipe_type in types:
            if len(self.recipes_list[recipe_type]) == 0:
                print('No recipe for ' + recipe_type)
            for elem in self.recipes_list[recipe_type]:
                print(str(elem))
            return self.recipes_list[recipe_type]
        print('Unknown recipe type')
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) != Recipe:
            raise ValueError("error: argument must be a Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        pass
