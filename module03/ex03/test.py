from ColorFilter import ColorFilter
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    cf = ColorFilter()

    for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
        arr = plt.imread("../resources/elon_canaGAN.png")
        plt.imshow(f(arr))
        plt.show()
    # cf.invert(arr)
    # cf.to_green(arr)
    # cf.to_red(arr)
    # cf.to_blue(arr)
    # cf.to_celluloid(arr)
    # cf.to_grayscale(arr, ’m’)
    # cf.to_grayscale(arr, ’weighted’, [0.2, 0.3, 0.5])
    # im = cf.to_grayscale(array, "m")
    # plt.imshow(im, cmap="gray")
    # plt.show()

    # im = cf.to_grayscale(array, "w", weights = [0.2126, 0.7152, 0.0722])
    # plt.imshow(im, cmap="gray")
    # plt.show()

    print("\nERROR:")
