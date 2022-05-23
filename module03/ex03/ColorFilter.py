import numpy as np


class ColorFilter:
    def __init__(self) -> None:
        pass

    def check_valid_array(self, array):
        if isinstance(array, np.ndarray) is False:
            return False
        elif len(array.shape) != 3:
            return False
        elif array.shape[2] < 3:
            return False
        return True

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None
        for z in range(3):
            array[:, :, z] = 1.0 - array[:, :, z]
        return array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None
        array[:, :, (0, 1)] = 0
        return array

        
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None
        array[:, :, (0, 2)] = 0
        return array

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None
        array[:, :, (2, 1)] = 0
        return array

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        if self.check_valid_array(array) is False:
            return None
