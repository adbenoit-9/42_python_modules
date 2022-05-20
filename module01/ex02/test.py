from vector import Vector

v1 = Vector([-1.0, 0.0, 1.0, 2.0])
v2 = Vector([0.0, 1.0, 2.0, 3.0])
v4 = Vector(-1, 3)
v5 = Vector(4)
print("v1 = {}".format(repr(v1)))
print("v2 = {}".format(repr(v2)))
print("v4 = {}".format(repr(v4)))
print("v5 = {}".format(repr(v5)))
try:
    print(repr(v1 * 2.0))
    print(repr(v4 * 2.0))
    print(repr(2 * v1))
    print(repr(2 * v4))
    print(repr(v1 / 2.0))
    print(repr(v4 / 2.0))
    print(repr(v1 + v2))
    print(repr(v4 + v5))
    print(repr(v1 - v2))
    print(repr(v4 - v5))
    print(v1.dot(v2))
    print(v4.dot(v5))
    print(repr(v1.T()))
    print(repr(v4.T()))
    2 / v1
except ValueError as err:
    print(err.args[0])
v3 = Vector(5, 10)
print(repr(v3))
try:
    v3 + v1
except ValueError as err:
    print(err.args[0])
v3 = Vector(3)
print(repr(v3))
try:
    v3 + 1
except ValueError as err:
    print(err.args[0])
try:
    v3 * v1
except ValueError as err:
    print(err.args[0])
