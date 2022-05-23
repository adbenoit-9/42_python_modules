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
        new_arr = 0 + array
        for z in range(3):
            new_arr[:, :, z] = 1.0 - new_arr[:, :, z]
        return new_arr

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        """
        new_arr = np.zeros(array.shape)
        new_arr = np.dstack([array])
        if self.check_valid_array(array) is False:
            return None
        new_arr[:, :, (0, 1)] = 0
        return new_arr

        
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
        new_arr = array.copy()
        new_arr[:, :, (0, 2)] = 0
        return new_arr

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
        new_arr = 0 + array
        new_arr[:, :, (2, 1)] = 0
        return new_arr

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
        shades = np.linspace(0, 1, 4)
        # for i in shades:

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
        if filter == 'm' or filter == 'mean':
            if len(kwargs.keys()) != 0:
                return None
            weights = [1 / 3, 1 / 3, 1 / 3]
        elif filter == 'w' or filter == 'weight':
            if len(kwargs.keys()) != 1 or 'weights' not in kwargs.keys():
                return None
            weights = kwargs['weights']
            if isinstance(weights, list) is False:
                return None
            elif len(weights) != 3 or sum(weights) != 1:
                return None
            for x in weights:
                if isinstance(x, float) is False:
                    return None
        else:
            return None
        new_arr = np.tile(array, 1)
        for y in range(array.shape[0]):
            for x in range(array.shape[1]):
                new_arr[y, x] = sum(array[y, x, :3] * weights)
        return new_arr[..., :3]
