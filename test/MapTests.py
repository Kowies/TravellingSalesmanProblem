import unittest
from lib.Map import euclidean_distance, Map


class DistanceTests(unittest.TestCase):
    def test_euklidean_distance_1(self):
        p1 = (1, 2)
        p2 = (2, 2)
        self.assertEqual(euclidean_distance(p1, p2), 1)


class MapTests(unittest.TestCase):
    def test_map_init(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4)]

        points_map = Map(points=points)

        self.assertEqual(points_map.get_point(0), (1, 1))
        self.assertEqual(points_map.get_point(3), (4, 4))

    def test_distance_different_points(self):
        points = [(1, 1), (1, 2), (3, 3), (4, 4)]

        points_map = Map(points=points, distance_function='euclidean')

        self.assertEqual(points_map.distance(0, 1), 1)
        self.assertEqual(points_map.distance(
            1, 2), euclidean_distance(points[1], points[2]))

    def test_distance_same_point(self):
        '''test if the distance between same points is zero'''
        points = [(1, 1), (1, 2), (3, 3), (4, 4)]

        points_map = Map(points=points, distance_function='euclidean')

        self.assertEqual(points_map.distance(0, 0), 0)
        self.assertEqual(points_map.distance(2, 2), 0)


if __name__ == '__main__':
    unittest.main()
