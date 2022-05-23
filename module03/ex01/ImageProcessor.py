import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

class ImageProcessor:
    def load(self, path):
        try:
            img = plt.imread(path)
            print("Loading image of dimensions {} x {}".format(*img.shape))
            return img
        except Exception as err:
            print('Exception: {}'.format(err))
            return None

    def display(self, array):
        fig, ax = plt.subplots()
        ax.imshow(array)
        ax.axis('off')
        plt.show()
