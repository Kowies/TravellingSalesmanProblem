import numpy as np


class GraphicalTSP():
    def __init__(self, points):
        self._data = np.array(points)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
