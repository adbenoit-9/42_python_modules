import sys

def operations(a, b):
    print("Sum: " + str(a + b)
    + "\nDifference: " + str(a - b)
    + "\nProduct: " + str(a * b))
    if b != 0:
        print("Quotient: " + str(a / b)
            + "\nRemainder: " + str(a % b))
    else:
            print("Quotient: ERROR (div by zero)"
                + "\nRemainder: ERROR (modulo by zero)") 
    return

usage="Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
if len(sys.argv) == 1:
    print(usage)
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n\n" + usage)
else:
    try:
        operations(int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
        print("InputError: only numbers\n\n" + usage)

