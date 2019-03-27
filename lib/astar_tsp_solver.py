from .tsp_solver import TSPSolver
from .tsp_state import TSPState
import heapq


class AStarTSPSolver(TSPSolver):
    def __init__(self, tsp):
        self.tsp = tsp

    def solve(self, state_class=TSPState):
        initial_state = state_class.initial_state(0, self.tsp)
        pqueue = [initial_state]
        while len(pqueue) != 0:
            current = heapq.heappop(pqueue)
            if current.is_final_state():
                return current.reconstruct_path(), current.length

            for state in current.extend():
                heapq.heappush(pqueue, state)
