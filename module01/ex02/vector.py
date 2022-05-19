class Vector:
    def __init__(self, *args):
        self.values = []
        if len(args) == 1 and isinstance(args[0], list):
            n = len(args[0])
            if n == 0:
                self.shape = (0, 0)
            elif len(args[0][0]) != 1:
                self.shape = (len(args[0][0]), 1)
                self.values = (args[0].copy())
            else:
                self.shape = (1, n)
                for i in args[0]:
                    self.values.append(i.copy())
        elif len(args) == 1:
            self.shape = (args[0], 1)
            for i in range(args[0]):
                self.values.append([float(i)])
        elif len(args) == 2:
            self.shape = (args[1] - args[0], 1)
            for i in range(args[0], args[1]):
                self.values.append([float(i)])
        else:
            raise ValueError('error')

    def __add__(self, v):
        if isinstance(v, Vector) is False or self.shape != v.shape:
            raise ValueError("Vectors must have the same dimensions.")
        res = []
        for i in range(self.shape[1]):
            res.append(self.values[i].copy())
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                res[i][j] += v.values[i][j]
        return Vector(res)

    def __radd__(self, v):
        return self.__add__(v)

    def __sub__(self, v):
        if isinstance(v, Vector) is False or self.shape != v.shape:
            raise ValueError("Vectors must have the same dimensions.")
        res = []
        for i in range(self.shape[1]):
            res.append(self.values[i].copy())
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                res[i][j] -= v.values[i][j]
        return Vector(res)

    def __rsub__(self, v):
        return self.__sub__(v)

    def __mul__(self, n):
        if isinstance(n, float) is False and isinstance(n, int) is False:
            raise ValueError("A Vector can be multiplied only by scalar.")
        res = []
        for i in range(self.shape[1]):
            res.append(self.values[i].copy())
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                res[i][j] *= n
        return Vector(res)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, float) is False and isinstance(n, int) is False:
            raise ValueError("A Vector can be divided only by scalar.")
        res = []
        for i in range(self.shape[1]):
            res.append(self.values[i].copy())
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                res[i][j] /= n
        return Vector(res)

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
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                res += self.values[i][j] * v.values[i][j]
        return res

    def T(self):
        res = []
        if self.shape[0] == 1:
            res.append([])
            for i in range(self.shape[1]):
                res[0].append(self.values[i][0])
        else:
            for i in range(self.shape[0]):
                res.append([self.values[0][i]])
        return Vector(res)
