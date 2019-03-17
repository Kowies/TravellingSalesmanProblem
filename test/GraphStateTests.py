import unittest
from lib.Map import Map
from lib.GraphState import GraphState


class GraphStateTests(unittest.TestCase):
    def setUp(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.point_map = Map(points=points)

    def test_initial_state(self):
        initial_state = GraphState.initial_state(1, self.point_map)

        self.assertEqual(initial_state.path, [1])
        self.assertEqual(initial_state.length, 0)

    def test_new_state_with_new_point(self):
        initial_state = GraphState.initial_state(1, self.point_map)

        new_state = initial_state.add_point(3)

        self.assertSequenceEqual(new_state.path, [1, 3])
        self.assertEqual(new_state.length,
                         self.point_map.distance_function((2, 2), (4, 4)))

    def test_extend(self):
        initial_state = GraphState.initial_state(2, self.point_map)

        new_states = initial_state.extend()

        self.assertTrue(initial_state.add_point(1) in new_states)
        self.assertTrue(initial_state.add_point(0) in new_states)
        self.assertTrue(initial_state.add_point(3) in new_states)
        self.assertFalse(initial_state.add_point(2) in new_states)

    def test_extend_with_final_state(self):
        initial_state = GraphState.initial_state(0, self.point_map)

        final_state = initial_state.add_point(1).add_point(2).add_point(3)

        self.assertEqual(final_state.extend(), [])

    def test_final_state(self):
        initial_state = GraphState.initial_state(0, self.point_map)

        not_final_state = initial_state.add_point(1).add_point(2)
        final_state = not_final_state.add_point(3)

        self.assertFalse(not_final_state.is_final_state())
        self.assertTrue(final_state.is_final_state())
