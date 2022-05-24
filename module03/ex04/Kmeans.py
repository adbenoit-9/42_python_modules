import sys
import numpy as np
import random as rd


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        if isinstance(max_iter, int) is False or \
                isinstance(ncentroid, int) is False:
            raise ValueError('invalid arguments')
        if max_iter < 0 or ncentroid < 0:
            raise ValueError('invalid arguments')
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids,
        random pick ncentroids from the datasetset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(X, np.ndarray) is False:
            return None
        if X.shape[0] < self.ncentroid:
            return None
        self.centroids = np.empty((self.ncentroid, 3))
        random_tab = []
        for i in range(self.ncentroid):
            index = rd.randint(0, X.shape[0] - 1)
            while index in random_tab:
                index = rd.randint(0, X.shape[0] - 1)
            random_tab.append(index)
            self.centroids[i] = X[index]
        for iter in range(self.max_iter):
            cluster = [[] for _ in range(self.ncentroid)]
            for i, point in enumerate(X):
                dist = np.empty(self.ncentroid)
                for j, centroid in enumerate(self.centroids):
                    dist[j] = np.linalg.norm(point - centroid)
                cluster[np.argmin(dist)].append(point)
            tmp = self.centroids.copy()
            for i in range(self.ncentroid):
                cluster[i] = np.array(cluster[i])
                if len(cluster[i]) != 0:
                    n = len(cluster[i])
                    self.centroids[i] = np.sum(cluster[i], axis=0) / n
            if (tmp == self.centroids).all():
                return None
        return None

    def predict(self, X):
        """
        Predict from wich cluster each datasetpoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(X, np.ndarray) is False or \
                len(self.centroids) != self.ncentroid:
            return None
        predict = []
        for point in X:
            dist = np.empty(self.ncentroid)
            for j, centroid in enumerate(self.centroids):
                dist[j] = np.linalg.norm(point - centroid)
            predict.append(self.centroids[np.argmin(dist)])
        return np.array(predict)


def parse_arg(argv):
    names = ['filepath', 'max_iter', 'ncentroid']
    if len(argv) != 4:
        return None
    new_args = {}
    for i in range(1, len(argv)):
        tmp = argv[i].split('=')
        if len(tmp) != 2 or tmp[0] not in names:
            return None
        new_args[tmp[0]] = tmp[1]
    for name in names:
        if name not in new_args.keys():
            return None
    try:
        new_args['max_iter'] = int(new_args['max_iter'])
        new_args['ncentroid'] = int(new_args['ncentroid'])
    except Exception:
        return None
    if new_args['max_iter'] < 0 or new_args['ncentroid'] < 0:
        return None
    return new_args


def parse_dataset(path):
    try:
        file = open(path, 'r')
    except Exception:
        return None
    lines = file.read().splitlines()
    dataset = []
    for i in range(1, len(lines)):
        dataset.append(lines[i].split(','))
        dataset[i - 1].pop(0)
        for j in range(len(dataset[i - 1])):
            try:
                dataset[i - 1][j] = float(dataset[i - 1][j].strip("'"))
            except Exception:
                return None
    return np.array(dataset)


def get_areas(kc):
    if kc.ncentroid != 4:
        return None
    i = np.argmax(kc.centroids[:, 0])
    belt = kc.centroids[i]
    tmp = kc.centroids.copy()
    tmp = np.delete(tmp, i, 0)
    earth = tmp.copy()
    earth = np.delete(earth, np.argmax(tmp[:, 0]), 0)
    i = np.argmin(tmp[:, 1])
    if (tmp[i] == earth[0]).all():
        earth = earth[1]
    else:
        earth = earth[0]
    for i in range(len(tmp)):
        if (tmp[i] == earth).all():
            tmp = np.delete(tmp, i, 0)
            break
    if (tmp[:, 1] < earth[1]).all() is False:
        i = np.argmin(tmp[:, 1])
        venus = tmp[i]
        mars = tmp[1 - i]
    else:
        i = np.argmax(tmp[:, 0])
        mars = tmp[i]
        venus = tmp[1 - i]
    areas = [[] for _ in range(kc.ncentroid)]
    ibelt = np.where(np.all(kc.centroids == belt, axis=1))[0][0]
    iearth = np.where(np.all(kc.centroids == earth, axis=1))[0][0]
    imars = np.where(np.all(kc.centroids == mars, axis=1))[0][0]
    ivenus = np.where(np.all(kc.centroids == venus, axis=1))[0][0]
    areas[iearth] = "Asteroids' Belt colonies"
    areas[ibelt] = "United Nations of Earth"
    areas[imars] = "Mars Republic"
    areas[ivenus] = "The flying cities of Venus"
    return areas


def display_info(kc, predict):
    if isinstance(predict, np.ndarray) is False:
        return None
    if kc.ncentroid == 4:
        areas = get_areas(kc)
        print('Coordinates of the different centroids and his region:')
        for i in range(kc.ncentroid):
            print('{} - {}'.format(kc.centroids[i], areas[i]))
        print()
    print('Number of individuals associated to each centroid:')
    for i in range(kc.ncentroid):
        count = 0
        for j in range(len(predict)):
            if (predict[j] == kc.centroids[i]).all():
                count += 1
        print('{} - {}'.format(kc.centroids[i], count))


if __name__ == "__main__":
    args = parse_arg(sys.argv)
    if args is not None:
        dataset = parse_dataset(args['filepath'])
        if dataset is not None:
            kc = KmeansClustering(args['max_iter'], args['ncentroid'])
            kc.fit(dataset)
            predict = kc.predict(dataset)
            if predict is None:
                print('ERROR')
            display_info(kc, predict)
        else:
            print('ERROR')
    else:
        print('ERROR')
