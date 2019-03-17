import unittest
from lib.Map import Map
from lib.GraphState import GraphState


class GraphStateTests(unittest.TestCase):
    def setUp(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.point_map = Map(points=points)

    def test_initial_state(self):
        initial_state = GraphState.initial_state(1)

        self.assertEqual(initial_state.path, [1])
        self.assertEqual(initial_state.length, 0)

    def test_new_state_with_new_point(self):
        initial_state = GraphState.initial_state(1)

        new_state = initial_state.add_point(3, self.point_map)

        self.assertSequenceEqual(new_state.path, [1, 3])
        self.assertEqual(new_state.length,
                         self.point_map.distance_function((2, 2), (4, 4)))

    def test_extend(self):
        initial_state = GraphState.initial_state(2)

        new_states = initial_state.extend(self.point_map)

        self.assertTrue(initial_state.add_point(
            1, self.point_map) in new_states)
        self.assertTrue(initial_state.add_point(
            0, self.point_map) in new_states)
        self.assertTrue(initial_state.add_point(
            3, self.point_map) in new_states)
        self.assertFalse(initial_state.add_point(
            2, self.point_map) in new_states)

    def test_extend_with_final_state(self):
        initial_state = GraphState.initial_state(0)

        final_state = initial_state.add_point(1, self.point_map).add_point(
            2, self.point_map).add_point(3, self.point_map)

        self.assertEqual(final_state.extend(self.point_map), [])

    def test_final_state(self):
        initial_state = GraphState.initial_state(0)

        not_final_state = initial_state.add_point(
            1, self.point_map).add_point(2, self.point_map)
        final_state = not_final_state.add_point(3, self.point_map)

        self.assertFalse(not_final_state.is_final_state(self.point_map))
        self.assertTrue(final_state.is_final_state(self.point_map))
