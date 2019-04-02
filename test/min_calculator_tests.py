import unittest
from lib.tsp import TSP
from lib.min_calculator import MinCalculator


class TSPTests(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.tsp = TSP(points=self.points)

    def test_map_init(self):
        min_calculator = MinCalculator(self.tsp)

        self.assertEqual(min_calculator[0], self.tsp.distance(0, 1))
        self.assertEqual(min_calculator[1], self.tsp.distance(2, 1))
        self.assertEqual(min_calculator[2], self.tsp.distance(2, 3))
        self.assertEqual(min_calculator[3], self.tsp.distance(3, 4))
        self.assertEqual(min_calculator[4], self.tsp.distance(4, 3))


if __name__ == '__main__':
    unittest.main()
