import random as rd


def guess():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")
    x = rd.randint(1, 99)
    i = 1
    while 1:
        y = input("What's your guess between 1 and 99?\n>> ")
        try:
            z = int(y)
            if z < x:
                print('Too low!')
            elif z > x:
                print('Too high!')
            else:
                if x == 42:
                    print("""The answer to the ultimate question of life, \
the universe and everything is 42.""")
                if i != 1:
                    str = 'You won in {} attempts!'.format(i)
                    print('Congratulations, you\'ve got it!\n' + str)
                else:
                    print('Congratulations! You got it on your first try!')
                return
            i += 1
        except ValueError:
            if y == "exit":
                print('Goodbye!')
                return
            print("That's not a number.")


guess()
