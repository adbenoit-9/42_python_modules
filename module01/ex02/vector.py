from ast import arg


class Vector:
    def __init__(self, *args):
        self.values = []
        if len(args) == 1 and isinstance(args[0], list):
            n = len(args[0])
            if n == 0:
                self.shape = (0, 0)
            elif isinstance(args[0][0], list) is False:
                self.shape = (n, 1)
            else:
                self.shape = (1, n)
            for elem in args[0]:
                if isinstance(elem, float) or \
                        (isinstance(elem, list) and
                            isinstance(elem[0], float)):
                    self.values = args[0]
                else:
                    raise ValueError('Invalid Type')
            self.values = args[0]
        elif len(args) == 1 and isinstance(args[0], int) and args[0] > 0:
            self.shape = (args[0], 1)
            for i in range(args[0]):
                self.values.append([float(i)])
        elif len(args) == 2 and isinstance(args[0], int)\
                and isinstance(args[1], int)\
                and args[0] <= args[1]:
            self.shape = (args[1] - args[0], 1)
            for i in range(args[0], args[1]):
                self.values.append([float(i)])
        else:
            raise ValueError('Invalid argument(s)')

    def copy(self):
        if self.shape == (0, 0):
            return []
        cpy = []
        for elem in self.values:
            if isinstance(elem, list):
                cpy.append(elem.copy())
            else:
                cpy.append(elem)
        return Vector(cpy)

    def __add__(self, v):
        if isinstance(v, Vector) is False or self.shape != v.shape:
            raise ValueError("Vectors must have the same dimensions.")
        res = self.copy()
        for i, val in enumerate(v.values):
            if isinstance(val, list):
                res.values[i][0] += val[0]
            else:
                res.values[i] += val
        return res

    def __radd__(self, v):
        return self.__add__(v)

    def __sub__(self, v):
        if isinstance(v, Vector) is False or self.shape != v.shape:
            raise ValueError("Vectors must have the same dimensions.")
        res = self.copy()
        for i, val in enumerate(v.values):
            if isinstance(val, list):
                res.values[i][0] -= val[0]
            else:
                res.values[i] -= val
        return res

    def __rsub__(self, v):
        return self.__sub__(v)

    def __mul__(self, n):
        if isinstance(n, Vector):
            return self.dot(n)
        if isinstance(n, float) is False and isinstance(n, int) is False:
            raise ValueError("A Vector can be multiplied only by scalar.")
        res = self.copy()
        for i, val in enumerate(res.values):
            if isinstance(val, list):
                res.values[i][0] *= n
            else:
                res.values[i] *= n
        return res

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, float) is False and isinstance(n, int) is False:
            raise ValueError("A Vector can be divided only by scalar.")
        if n == 0:
            raise ValueError("Division by 0")
        res = self.copy()
        for i, val in enumerate(res.values):
            if isinstance(val, list):
                res.values[i][0] /= n
            else:
                res.values[i] /= n
        return res

    def __rtruediv__(self, n):
        raise ValueError("A scalar cannot be divided by a Vector.")

    def __repr__(self):
        return 'Vector({})'.format(self.values)

    def __str__(self):
        return 'Vector({})'.format(self.values)

    def dot(self, v):
        res = 0
        if isinstance(v, Vector) is False or self.shape != v.shape:
            raise ValueError("Vectors must have the same dimensions.")
        for i, val in enumerate(self.values):
            if isinstance(val, list):
                res += val[0] * v.values[i][0]
            else:
                res += val * v.values[i]
        return res

    def T(self):
        if self.shape == (0, 0):
            return []
        res = []
        for elem in self.values:
            if isinstance(elem, list):
                res.append(elem[0])
            else:
                res.append([elem])
        return Vector(res)
