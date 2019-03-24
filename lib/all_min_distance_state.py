from .tsp_state import TSPState


class AllMinHeuristicState(TSPState):
    '''
    this heuristic returns the minimal distance of all
    unvisited vertecies to their neighbors
    times the number of unvisited vertecies
    '''

    def __init__(self, path, length, tsp, heuristic_info=None):
        super().__init__(path, length, tsp)
        self.heuristic_info = heuristic_info

    @staticmethod
    def initial_state(initial_point_index, tsp):
        return AllMinHeuristicState((initial_point_index,), 0, tsp)

    def _add_point(self, point_index):
        new_state = super()._add_point(point_index)

        if self.heuristic_info:
            heuristic_value, min_vetex_index, non_visited_len = self.heuristic_info
            if min_vetex_index != point_index:
                new_heuristic = ((non_visited_len - 1) * (heuristic_value /
                                                          non_visited_len), min_vetex_index, non_visited_len - 1)
                new_state.heuristic_info = new_heuristic

        return new_state

    def _calculate_heuristic(self):
        if self.is_final_state():
            self.heuristic_info = (0, 0, 0)
            return

        non_visited_vertecies = self._get_non_visited_point_idexes()
        min_distance = min([(self.tsp.distance(other_vertex, vertex), vertex)
                            for vertex in non_visited_vertecies
                            for other_vertex in range(self.tsp.get_points_count())
                            if vertex != other_vertex])

        self.heuristic_info = (
            min_distance[0] * len(non_visited_vertecies),  # heuristic value
            min_distance[1],  # vertex index
            len(non_visited_vertecies),
        )

    def heuristic(self):
        if not self.heuristic_info:
            self._calculate_heuristic()

        return self.heuristic_info[0]
