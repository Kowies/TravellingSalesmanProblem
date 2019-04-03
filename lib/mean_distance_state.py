from .tsp_state import TSPState
import numpy as np


class MeanDistanceState(TSPState):
    '''
    this heuristic returns distance to the closest vertex
    times the number of unvisited vertecies
    '''

    def __init__(self, path, length, tsp, mean=None):
        super().__init__(path, length, tsp)
        self.mean = mean

    @staticmethod
    def initial_state(initial_point_index, tsp):
        mean = np.mean(tsp.dist_map)
        return MeanDistanceState((initial_point_index,), 0, tsp, mean)

    def _add_point(self, point_index):
        new_state = super()._add_point(point_index)
        new_state.mean = self.mean
        return new_state

    def heuristic(self):
        return len(self._get_non_visited_point_idexes()) * self.mean
