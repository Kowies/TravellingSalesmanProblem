import unittest
from lib.tsp import TSP
from lib.tsp_state import TSPState


class TSPStateTests(unittest.TestCase):
    def setUp(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.tsp = TSP(points=points)

    def test_initial_state(self):
        initial_state = TSPState.initial_state(1, self.tsp)

        self.assertEqual(initial_state.path, (1,))
        self.assertEqual(initial_state.length, 0)

    def test_new_state_with_new_point(self):
        initial_state = TSPState.initial_state(1, self.tsp)

        new_state = initial_state._add_point(3)

        self.assertSequenceEqual(new_state.path, [1, 3])
        self.assertEqual(new_state.length,
                         self.tsp.distance_function((2, 2), (4, 4)))

    def test_extend(self):
        initial_state = TSPState.initial_state(2, self.tsp)

        new_states = initial_state.extend()

        self.assertTrue(initial_state._add_point(1) in new_states)
        self.assertTrue(initial_state._add_point(0) in new_states)
        self.assertTrue(initial_state._add_point(3) in new_states)
        self.assertFalse(initial_state._add_point(2) in new_states)

    def test_extend_with_final_state(self):
        initial_state = TSPState.initial_state(0, self.tsp)

        final_state = initial_state._add_point(1)._add_point(2)._add_point(3)

        self.assertEqual(final_state.extend(), [])

    def test_final_state(self):
        initial_state = TSPState.initial_state(0, self.tsp)

        not_final_state = initial_state._add_point(1)._add_point(2)
        final_state = not_final_state._add_point(3)

        self.assertFalse(not_final_state.is_final_state())
        self.assertTrue(final_state.is_final_state())
