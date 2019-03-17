import numpy as np


class GraphState():
    """
    GraphState represent one of the states of the graph. Class holds
    the state defining values like
        1)length of the taken path
        2)number of points visited
        3)a path(ordered list of point indexes)

    ...

    Attributes
    ----------
    path : array[point_idex]
        ordered array of point indexes representing current path
    length : float
        length of a whole path up to the last point
    """

    def __init__(self, path=[], length=0, point_map=None):
        '''
        Parameters
        ----------
        path : array[point]
            a path that will be represented by the graph state
        length: float
            length of a new GraphState
        point_map: Map
            Map object representing of all the points
        '''
        self.path = path
        self.length = length
        self.point_map = point_map

    def __eq__(self, other):
        return self.path == other.path and self.length == other.length

    def __str__(self):
        return str(self.path) + ', ' + str(self.length)

    @staticmethod
    def initial_state(point_index, point_map):
        return GraphState([point_index], point_map=point_map)

    def add_point(self, point_index):
        '''
        return new GraphState with new point added to path
        Parameters
        ----------
        point_index : point index
            new point index that wants to be added to the path
        Returns
        -------
        GrapState
            new graph state with updated path
        '''
        new_path = self.path + [point_index]
        new_length = self.length + \
            self.point_map.distance(self.path[-1], point_index)
        return GraphState(new_path, new_length, self.point_map)

    def extend(self):
        '''
        returns all of the states that can be reached from the current state
        Returns
        -------
        Array[GraphState]
            array of possible states
        '''
        path_set = set(self.path)
        return [self.add_point(point) for point in range(
            self.point_map.get_points_count()) if point not in path_set]

    def is_final_state(self):
        '''
        boolean indicating if state is a final state
        Parameters
        ----------
        Returns
        -------
        boolean
            true if state is final state false if not
        '''
        return len(self.path) == self.point_map.get_points_count()

    def reconstruct_path(self):
        '''
        Returns the exact ordered list of points from initial state
        to final state
        Returns
        -------
        array[point]
            array of points(2-tuples) representing the path
        '''
        return [self.point_map.get_point(point_id) for point_id in self.path]
