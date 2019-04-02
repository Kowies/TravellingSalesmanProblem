from lib.tsp_state import TSPState
from collections import deque
from lib.tsp_solver import TSPSolver


class BruteTSP(TSPSolver):
    def __init__(self, tsp):
        self.initial_state = TSPState.initial_state(0, tsp=tsp)

    def solve(self):
        best_trip = None
        queue = deque([self.initial_state])

        visited_count = 0
        while len(queue) > 0:
            current_state = queue.pop()
            visited_count += 1

            if current_state.is_final_state():
                if best_trip == None or current_state.length < best_trip.length:
                    best_trip = current_state

            queue.extend(current_state.extend())

        return best_trip.reconstruct_path(), best_trip.length, visited_count
