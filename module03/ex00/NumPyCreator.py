import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def check_nested_seq(self, seq):
        if len(seq) == 0:
            return True
        is_nested = False
        for i, x in enumerate(seq):
            if isinstance(x, tuple) or isinstance(x, list):
                is_nested = True
                break
        if is_nested is False:
            return True
        for x in seq:
            if isinstance(x, type(seq[i])) is False:
                return False
            elif len(x) != len(seq[i]):
                return False
        return True

    def from_list(self, lst):
        if isinstance(lst, list) is False:
            return None
        elif self.check_nested_seq(lst) is False:
            return None
        return np.array(lst)

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple) is False:
            return None
        elif self.check_nested_seq(tpl) is False:
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        if isinstance(itr, tuple):
            return self.from_tuple(itr)
        elif isinstance(itr, list):
            return self.from_list(itr)
        try:
            iter(itr)
        except Exception:
            return None
        return np.array(itr)

    def from_shape(self, shape, value=0):
        if isinstance(shape, tuple) is False:
            return None
        elif len(shape) != 2:
            return None
        elif isinstance(shape[0], int) is False or \
                isinstance(shape[1], int) is False:
            return None
        elif shape[0] < 0 or shape[1] < 0:
            return None
        return np.full(shape, value)

    def random(self, shape):
        if isinstance(shape, tuple) is False:
            return None
        elif len(shape) != 2:
            return None
        elif isinstance(shape[0], int) is False or \
                isinstance(shape[1], int) is False:
            return None
        elif shape[0] < 0 or shape[1] < 0:
            return None
        return np.random.rand(shape[0], shape[1])

    def identity(self, n):
        if isinstance(n, int) is False:
            return None
        elif n < 0:
            return None
        return np.identity(n)
