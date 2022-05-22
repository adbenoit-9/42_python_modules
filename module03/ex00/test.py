from NumPyCreator import NumPyCreator

if __name__ == '__main__':
    npc = NumPyCreator()
    print(npc.from_list([[], []]))
    print(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    print(npc.from_shape((0, 0)))
    print(npc.from_shape((3, 5)))
    print(npc.random((3, 5)))
    print(npc.identity(4))
    print()

    print("ERROR:")
    print(npc.from_list("toto"))
    print(npc.from_list([[1, 2, 3], [6, 3, 4], [8, 5, 6, 7]]))
    print(npc.from_list([[1, 2, 3], [6, 3, 4], None]))
    print(npc.from_list([None, [6, 3, 4], [8, 5, 6, 7]]))
    print(npc.from_tuple(3.2))
    print(npc.from_tuple(((1, 5, 8), (7, 5))))
    print(npc.from_shape((-1, -1)))
    print(npc.identity(-1))
