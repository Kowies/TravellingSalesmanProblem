from lib.min_vertex_heuristic_state import MinVertexHeuristicState
from lib.tsp import TSP
import unittest
import math


class MinHeuristicTest(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.tsp = TSP(points=self.points)

    def test_auto_heuristic_calculation_test(self):
        '''testing initial auto calculating heuristic value'''
        initial_state = MinVertexHeuristicState.initial_state(0, self.tsp)

        heuristic_value = initial_state.heuristic()

        min_distance = self.tsp.distance_function(
            self.points[0], self.points[1])
        self.assertAlmostEqual(heuristic_value, min_distance * 4)

    def test_forward_no_min_heuristic_calculation_test_2(self):
        '''
        testing calculating heuristic value that is based on previous state
        no min means that heuristic is forwarded(not calculated by _calculate_heuristic)
        '''
        initial_state = MinVertexHeuristicState.initial_state(0, self.tsp)
        next_state = initial_state._add_point(4)

        heuristic_value = next_state.heuristic()

        min_distance = self.tsp.distance_function(
            self.points[0], self.points[1])
        self.assertAlmostEqual(heuristic_value, min_distance * 3)

    def test_forward_min_heuristic_calculation_test_2(self):
        '''
        testing calculating heuristic value that is based on previous state
        min means that heuristic is not forwarded(calculated by _calculate_heuristic)
        '''
        initial_state = MinVertexHeuristicState.initial_state(0, self.tsp)
        next_state = initial_state._add_point(1)

        heuristic_value = next_state.heuristic()

        min_distance = self.tsp.distance_function(
            self.points[1], self.points[2])
        self.assertAlmostEqual(heuristic_value, min_distance * 3)


if __name__ == '__main__':
    unittest.main()
