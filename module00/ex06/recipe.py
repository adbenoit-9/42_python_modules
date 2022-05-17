import sys

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salade': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_recipe(name):
    if name in cookbook:
        print('\nRecipe for {}:'.format(name))
        sys.stdout.write('Ingredients lists: ')
        print(cookbook[name]['ingredients'])
        print('To be eaten for {}.'.format(cookbook[name]['meal']))
        print('Takes {} minutes of cooking.'
              .format(cookbook[name]['prep_time']))
    else:
        print('\nRecipe {} doesn\'t exist'.format(name))
    return


def delete_recipe(name):
    if name in cookbook:
        cookbook.pop(name)


def add_recipe(name, ingr, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingr,
        'meal': meal,
        'prep_time': prep_time
    }
    return


def print_all_recipe():
    for key in cookbook.keys():
        print_recipe(key)


str = """Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit"""

while 1:
    print(str)
    x = input('>> ')
    if x == "1":
        name = input("\nPlease enter the recipe's name: ")
        ingr = input("ingredients list: ")
        meal = input("meal type: ")
        prep_time = input("preparation time in minutes: ")
        ingr_list = ingr.split()
        try:
            add_recipe(name, ingr_list, meal, int(prep_time))
            print('\n{} added to the cookbook !'.format(name))
        except ValueError:
            print('\nInput error: preparation time value invalid.')
    elif x == "2":
        name = input("\nPlease enter the recipe's name:\n>> ")
        delete_recipe(name)
        print('\n{} deleted of the cookbook !'.format(name))
    elif x == "3":
        name = input("""\nPlease enter the recipe's name to get \
its details:\n>> """)
        print_recipe(name)
    elif x == "4":
        print('\n-- COOKBOOK --')
        print_all_recipe()
    elif x == "5":
        print('\nCookbook closed.')
        break
    else:
        print("""\nThis option does not exist, please type the \
corresponding number.\nTo exit, enter 5.""")
    print("")
