import unittest
from lib.tsp import TSP
from lib.brute_tsp import BruteTSP


class BruteTSPTests(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.tsp = TSP(points=self.points)

    def test_correct_solve(self):
        brute = BruteTSP(self.tsp)

        result = brute.solve()

        self.assertListEqual(result, self.points)
