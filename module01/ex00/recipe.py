class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if isinstance(name, str) is False or len(name) == 0:
            raise ValueError("error: recipe name must be a none empty string")
        elif isinstance(cooking_lvl, int) is False or cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("error: cooking level must be an int between 1 and 5")
        elif isinstance(cooking_time, int) is False or cooking_time < 0:
            raise ValueError("error: cooking time must be in minutes")
        elif isinstance(ingredients, list) is False or len(ingredients) == 0:
            raise ValueError("error: ingredients must be a none empty list")
        elif isinstance(name, str) is False or (recipe_type != "starter"
                and recipe_type != "lunch" and recipe_type != "dessert"):
            raise ValueError("error: invalid recipe type")
        elif isinstance(description, str) is False:
            raise ValueError("error: invalid description")
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
