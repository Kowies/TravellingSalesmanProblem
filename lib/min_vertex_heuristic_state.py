from .tsp_state import TSPState


class MinVertexHeuristicState(TSPState):
    '''
    this heuristic returns distance to the closest vertex
    times the number of unvisited vertecies
    '''

    def __init__(self, path, length, tsp):
        super().__init__(path, length, tsp)
        self.heuristic_info = None

    @staticmethod
    def initial_state(initial_point_index, tsp):
        return MinVertexHeuristicState((initial_point_index,), 0, tsp)

    def _calculate_heuristic(self):
        if self.is_final_state():
            self.heuristic_info = 0
            return

        non_visited_vertecies = self._get_non_visited_point_idexes()
        min_distance = min([self.tsp.distance(self.path[-1], vertex)
                            for vertex in non_visited_vertecies])
        self.heuristic_info = min_distance * len(non_visited_vertecies)

    def heuristic(self):
        if not self.heuristic_info:
            self._calculate_heuristic()

        return self.heuristic_info
