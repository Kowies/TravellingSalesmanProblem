"""
Map represents the map of all points in the problem.
"""
import numpy as np


def euclidean_distance(a, b):
    '''
    Calculates the euclidean distance between two points(2-tuples)
    Parameters
    ----------
    a,b : points
        points to calculate distance between them
    Returns
    -------
    float
        euclidean distance between points
    '''
    diff_x = (a[0] - b[0])
    diff_y = (a[1] - b[1])
    return np.sqrt(diff_x*diff_x + diff_y*diff_y)


class TSP():
    def __init__(self, points=None, distance_function='euclidean'):
        '''
        Builds the map from the file given in filename kwarg
        or from array of points(2-tuples). Raises exception
        when none of arguments were specified
        '''
        if distance_function == 'euclidean':
            self.distance_function = euclidean_distance
        if points:
            self.points = points
        else:
            raise AttributeError('Data was not specified')

        self._build_dist_map()

    def _build_dist_map(self):
        '''
        builds 2d array of all given points. This array
        allows to retrieve the distance from point to
        any other point in the map
        '''
        self.dist_map = np.zeros([len(self.points), len(self.points)])

        for i, point_1 in enumerate(self.points):
            for j, point_2 in enumerate(self.points[:i]):
                dist = self.distance_function(point_1, point_2)
                self.dist_map[i, j] = self.dist_map[j, i] = dist

    def distance(self, point_index_1, point_index_2):
        '''
        Returns the distance between two points identified by their id's
        Parameters
        ----------
        point_index_1,point_index_2 : int
            id's of the points
        Returns
        -------
        float
            distance between two points
        '''
        return self.dist_map[point_index_1, point_index_2]

    def get_point(self, index):
        return self.points[index]

    def get_points_count(self):
        return len(self.points)
