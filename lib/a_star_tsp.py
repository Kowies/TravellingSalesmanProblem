import heapq

from lib.tsp import TSP
from lib.tsp_state import TSPState
from lib.tsp_solver import TSPSolver


class AStarTSP(TSPSolver):
    def __init__(self, tsp):
        self.initial_state = TSPState.initial_state(0, tsp=tsp)

    def solve(self):
        heap = []
        heapq.heappush(heap, self.initial_state)

        while len(heap) > 0:
            current_state = heapq.heappop(heap)

            if current_state.is_final_state():
                return current_state.reconstruct_path()
            else:
                for state in current_state.extend():
                    heapq.heappush(heap, state)

