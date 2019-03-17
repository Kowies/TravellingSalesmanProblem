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

    def __init__(self, path=[], length=0):
        '''
        Parameters
        ----------
        path : array[point]
            a path that will be represented by the graph state
        length: float
            length of a new GraphState
        '''
        self.path = path
        self.length = length

    def __str__(self):
        return str(self.path) + ', ' + str(self.length)

    @staticmethod
    def initial_state(point_index):
        return GraphState([point_index])

    def __eq__(self, other):
        return self.path == other.path and self.length == other.length

    def add_point(self, point_index, point_map):
        '''
        return new GraphState with new point added to path
        Parameters
        ----------
        point_index : point index
            new point index that wants to be added to the path
        point_map: Map
            point map
        Returns
        -------
        GrapState
            new graph state with updated path
        '''
        if not point_map:
            raise AttributeError(
                'You forgot to pass point_map argument to expand method')
        return GraphState(self.path + [point_index], self.length + point_map.distance(self.path[-1], point_index))

    def extend(self, point_map):
        '''
        returns all of the states that can be reached from the current state
        Parameters
        ----------
        point_map: Map
            point map
        Returns
        -------
        Array[GraphState]
            array of possible states
        '''
        path_set = set(self.path)
        return [self.add_point(point, point_map) for point in range(
            point_map.get_points_count()) if point not in path_set]

    def is_final_state(self, point_map):
        '''
        boolean indicating if state is a final state
        Parameters
        ----------
        point_map: Map
            point map
        Returns
        -------
        boolean
            true if state is final state false if not
        '''
        return len(self.path) == point_map.get_points_count()

    def reconstruct_path(self, point_map):
        '''
        Returns the exact ordered list of points from initial state
        to final state
        Parameters
        ----------
        point_map: Map
            point map
        Returns
        -------
        array[point]
            array of points(2-tuples) representing the path
        '''
        return [point_map.get_point(point_id) for point_id in self.path]
