import numpy as np


class ScrapBooker(object):
    def __init__(self) -> None:
        pass

    def is_valid_tuple(self, tpl):
        if isinstance(tpl, tuple) is False:
            return False
        elif len(tpl) != 2:
            return False
        elif isinstance(tpl[0], int) is False or \
                isinstance(tpl[0], int) is False:
            return False
        elif tpl[0] < 0 or tpl[1] < 0:
            return False
        return True

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False or \
                self.is_valid_tuple(dim) is False or \
                self.is_valid_tuple(position) is False:
                    return None
        xend = position[1] + dim[1]
        yend = position[0] + dim[0]
        return array[position[0]:yend, position[1]:xend]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Returns:
            new_arr: thined numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False or \
                isinstance(n, int) is False or \
                isinstance(axis, int) is False:
                    return None
        elif n <= 0 or (axis != 0 and axis != 1):
            return None
        return np.delete(array, n, 1 - axis)
        

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False or \
                isinstance(n, int) is False or \
                isinstance(axis, int) is False:
                    return None
        elif n <= 0 or (axis != 0 and axis != 1):
            return None
        new_arr = array.copy()
        for i in range(n):
            new_arr = np.concatenate((new_arr, array), axis)
        return new_arr

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False or \
                self.is_valid_tuple(dim) is False:
            return None
        new_arr = self.juxtapose(array, dim[0], 1)
        new_arr = self.juxtapose(new_arr, dim[1], 0)
        return new_arr
