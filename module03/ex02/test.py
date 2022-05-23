import numpy as np
from ScrapBooker import ScrapBooker

if __name__ == '__main__':
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    print(spb.crop(arr1, (3, 1), (1, 0)))
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    print(spb.thin(arr2, 3, 0))
    arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    print(spb.thin(arr3, 3, 1))
    arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(spb.juxtapose(arr4, 2, 0))
    print(spb.mosaic(arr4, (2, 3)))

    print("\nERROR:")
    not_numpy_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spb.crop(not_numpy_arr, (1, 2)))
    print(spb.crop(arr1, (1, 2), (-1, 4)))
    print(spb.crop(arr1, (1, 2), (1, -4)))
    print(spb.crop(arr1, (1, -2), (1, 4)))
    print(spb.crop(arr1, (-1, 2), (1, 4)))
    print(spb.crop(arr1, 1, (1, 4)))
    print(spb.crop(arr1, (1, 2), 1))
    print(spb.thin(arr3, -3, 1))
    print(spb.thin(arr3, 0, 1))
    print(spb.thin(arr3, 0, 2))
    print(spb.thin(not_numpy_arr, 0, 2))
    print(spb.juxtapose(arr3, -3, 1))
    print(spb.juxtapose(arr3, 0, 1))
    print(spb.juxtapose(arr3, 0, 2))
    print(spb.juxtapose(not_numpy_arr, 0, 2))
    print(spb.mosaic(arr4, (1, 2, 3)))
