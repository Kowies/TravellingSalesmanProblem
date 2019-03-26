import unittest
from lib.tsp import TSP
from lib.brute_tsp import BruteTSP


class BruteTSPTests(unittest.TestCase):

    def test_correct_solve_1(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        tsp = TSP(points)

        brute = BruteTSP(tsp)

        result = brute.solve()

        print(result)

        self.assertListEqual(result, points)


    def test_correct_solve_2(self):
        points = [(1, 12), (3, 2), (1, 3), (8, 2), (-1, 5)]
        tsp = TSP(points)

        brute = BruteTSP(tsp)

        result = brute.solve()

        print(result)

        self.assertListEqual([], []) #todo