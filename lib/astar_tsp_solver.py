from .tsp_solver import TSPSolver
from .tsp_state import TSPState
import heapq


def state_total_score(state):
    return state.heuristic() + state.length


class AStarTSPSolver(TSPSolver):
    def __init__(self, tsp):
        self.tsp = tsp

    def solve(self, initial_state=None):
        if initial_state == None:
            initial_state = TSPState.initial_state(0, self.tsp)

        pqueue = [initial_state]
        while len(pqueue) != 0:
            current = heapq.heappop(pqueue)
            if current.is_final_state():
                return current.reconstruct_path(), current.length

            for state in current.extend():
                heapq.heappush(pqueue, state)

        return None
