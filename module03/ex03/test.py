from ColorFilter import ColorFilter
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    cf = ColorFilter())

    for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
        arr = plt.imread("../resources/elon_canaGAN.png")
        plt.imshow(f(arr))
        plt.show()
        plt.imshow(arr, cmap="gray")
        plt.show()

    im = cf.to_grayscale(arr, "m")
    plt.imshow(im, cmap="gray")
    plt.show()
    plt.imshow(arr, cmap="gray")
    plt.show()

    im = cf.to_grayscale(arr, "w", weights = [0.2126, 0.7152, 0.0722])
    plt.imshow(im, cmap="gray")
    plt.show()
    plt.imshow(arr, cmap="gray")
    plt.show()

    print("\nERROR:")
    print(cf.to_grayscale(arr, "m", weights = [0.2126, 0.7152, 0.0722]))
    print(cf.to_grayscale(arr, "mean", weights = [0.2126, 0.7152, 0.0722]))
    print(cf.to_grayscale(arr, "w"))
    print(cf.to_grayscale(arr, "y"))
    print(cf.to_grayscale(arr, "w", test = [1., 2., 3.]))
    print(cf.to_grayscale(arr, "w", weights = ["hey", 2., 3.]))
    print(cf.to_grayscale(arr, "w", weights = [2., 3.]))