class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if len(name) == 0:
            raise ValueError("error: recipe name must not be empty")
        elif cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("error: cooking level must be between 1 and 5")
        elif cooking_time < 0:
            raise ValueError("error: cooking time must be in minutes")
        elif len(ingredients) == 0:
            raise ValueError("error: ingredients must not be empty")
        elif recipe_type != "starter" and recipe_type != "lunch"\
                and recipe_type != "dessert":
            raise ValueError("error: invalid recipe type")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients.copy()
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = """name:\t\t{name}
cooking level:\t{cooking_lvl}
cooking time:\t{cooking_time}
ingredients:\t{ingredients}
description:\t{description}
recipe type:\t{recipe_type}"""\
        .format(**self.__dict__)
        return txt
