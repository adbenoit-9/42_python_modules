from book import Book
from recipe import Recipe

b = Book("My seductive recipes")
try:
    Book(10)
except ValueError as err:
    print(err)
print(b.creation_date)
print(b.last_update)
b.get_recipes_by_types("lunch")
crumble = Recipe("Crumble", 1, 25, ["apples", "flour", "sugar"],
                 "delicious", "dessert")
b.add_recipe(crumble)
print(b.last_update)
b.get_recipe_by_name("Crumble")
b.get_recipe_by_name("Liver Icecream")
b.get_recipes_by_types("dessert")[0]
b.get_recipes_by_types("asdasd")
try:
    Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "", "dessert")
except ValueError as err:
    print(err)
try:
    Recipe("", 0, 1, ["dough", "sugar", "love"], "", "dessert")
except ValueError as err:
    print(err)
try:
    Recipe(4, 1, 10, ["dough", "sugar", "love"], "", "dessert")
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, 1, ["dough", "sugar", "love"], "", 1)
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, 1, ["dough", "sugar", "love"], "", "test")
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, 1, [], "", "lunch")
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, 1, 1, "deliciousness incarnate", "lunch")
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, 1, ['test'], 1, "lunch")
except ValueError as err:
    print(err)
try:
    Recipe("test", 1, -10, ['test'], "", "lunch")
except ValueError as err:
    print(err)

try:
    Recipe("cooki", 1, 10, ["dough", "sugar", "love"],
           "deliciousness incarnate", "dessert")
    print("Congratulations you finally made sime delicous cookies")
    Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"],
           "deliciousness incarnate", "dessert")
except ValueError as err:
    print(err)
