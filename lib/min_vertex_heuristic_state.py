from .tsp_state import TSPState


class MinVertexHeuristicState(TSPState):
    def __init__(self, path, length, tsp, heuristic_info=None):
        super().__init__(path, length, tsp)
        self.heuristic_info = heuristic_info

    @staticmethod
    def initial_state(initial_point_index, tsp):
        return MinVertexHeuristicState((initial_point_index,), 0, tsp)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.heuristic() + self.length < other.heuristic() + other.length

    def _add_point(self, point_index):
        new_path = self.path + (point_index,)
        new_length = self.length + \
            self.tsp.distance(self.path[-1], point_index)

        if self.heuristic_info:
            heuristic_value, min_vetex_index, non_visited_len = self.heuristic_info
            if min_vetex_index != point_index:
                new_heuristic = ((non_visited_len - 1) * (heuristic_value /
                                                          non_visited_len), min_vetex_index, non_visited_len - 1)
                return MinVertexHeuristicState(new_path, new_length, self.tsp,  heuristic_info=new_heuristic)

        return MinVertexHeuristicState(new_path, new_length, self.tsp)

    def _calculate_heuristic(self):
        if self.is_final_state():
            self.heuristic_info = (0, 0, 0)
            return

        non_visited_vertecies = self._get_non_visited_point_idexes()
        min_distance = min([(self.tsp.distance(self.path[-1], vertex), vertex)
                            for vertex in non_visited_vertecies])
        self.heuristic_info = (
            min_distance[0] * len(non_visited_vertecies),  # heuristic value
            min_distance[1],  # vertex index
            len(non_visited_vertecies),
        )

    def heuristic(self):
        if not self.heuristic_info:
            self._calculate_heuristic()

        return self.heuristic_info[0]
