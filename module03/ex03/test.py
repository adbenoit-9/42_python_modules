from ColorFilter import ColorFilter
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    cf = ColorFilter()
    for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
        arr = plt.imread("../ressources/elon_canaGAN.png")
        im = f(arr)
        if arr is None:
            print('failed')
        else:
            plt.imshow(im)
            plt.show()
    im = cf.to_grayscale(arr, "m")
    if im is None:
        print('failed')
    else:
        plt.imshow(im, cmap="gray")
        plt.show()

    im = cf.to_grayscale(arr, "w", weights=[0.2126, 0.7152, 0.0722])
    if im is None:
        print('failed')
    else:
        plt.imshow(im, cmap="gray")
        plt.show()

    im = cf.to_celluloid(arr)
    if im is None:
        print('failed')
    else:
        plt.imshow(im, cmap="gray")
        plt.show()

    print("\nERROR:")
    print(cf.to_grayscale(arr, "m", weights=[0.2126, 0.7152, 0.0722]))
    print(cf.to_grayscale(arr, "mean", weights=[0.2126, 0.7152, 0.0722]))
    print(cf.to_grayscale(arr, "mean", weights=[0.3, 0.7152, 0.0722]))
    print(cf.to_grayscale(arr, "w"))
    print(cf.to_grayscale(arr, "y"))
    print(cf.to_grayscale(arr, "w", test=[1., 2., 3.]))
    print(cf.to_grayscale(arr, "w", weights=["hey", 2., 3.]))
    print(cf.to_grayscale(arr, "w", weights=[2., 3.]))
