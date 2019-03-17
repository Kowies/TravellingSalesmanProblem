from lib.GraphState import GraphState
from collections import deque


class BruteTS():
    def __init__(self, point_map, initial_point=0):
        self.initial_state = GraphState.initial_state(initial_point, point_map)

    def compute_shortest_path(self):
        best_trip = None
        queue = deque([self.initial_state])
        while len(queue) > 0:
            current_state = queue.pop()
            if current_state.is_final_state():
                print(current_state)
            if current_state.is_final_state() and (not best_trip or current_state.length < best_trip.length):
                best_trip = current_state

            queue.extend(current_state.extend())

        return best_trip.reconstruct_path()
