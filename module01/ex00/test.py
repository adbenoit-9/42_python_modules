from book import Book
from recipe import Recipe

try:
    tourte = Recipe("tourte", 4, 30, ['eggs', 'milk', 'cheese'], ":)", "lunch")
    cake = Recipe("cake", 4, 60, ['flavour', 'chocalate'], ":D", "dessert")
    salade = Recipe("salade", 4, 0, ['avocado', 'tomatoes'], ":(", "lunch")
    book = Book("Cookbook")
    book.add_recipe(tourte)
    book.add_recipe(cake)
    book.add_recipe(salade)
    lunch = book.get_recipes_by_types("lunch")
    for recipe in lunch:
        print(str(recipe))
    print()
    cake_book = book.get_recipe_by_name('cake')
    print(str(cake_book))
except ValueError as error:
    print(error.args[0])
