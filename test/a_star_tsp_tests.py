import unittest
from lib.tsp import TSP
from lib.a_star_tsp import AStarTSP
from lib.brute_tsp import BruteTSP


class AStarTSPTests(unittest.TestCase):

    def test_correct_solve_1(self):
        points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        tsp = TSP(points)

        star = AStarTSP(tsp)
        brute = BruteTSP(tsp)

        result_star = star.solve()
        result_brute = brute.solve()

        self.assertListEqual(result_star, result_brute)


    def test_correct_solve_2(self):
        points = [(1, 12), (3, 2), (1, 3), (8, 2), (-1, 5)]
        tsp = TSP(points)

        star = AStarTSP(tsp)
        brute = BruteTSP(tsp)

        result_star = star.solve()
        result_brute = brute.solve()

        self.assertListEqual(result_star, result_brute)

    def test_correct_solve_3(self):
        points = [(1, 12), (3, 2), (1, 3), (8, 2), (-1, 5), (0, 0), (1,123)]
        tsp = TSP(points)

        star = AStarTSP(tsp)
        brute = BruteTSP(tsp)

        result_star = star.solve()
        result_brute = brute.solve()

        self.assertListEqual(result_star, result_brute)

    def test_correct_solve_4(self):
        points = [(0, 0), (1, 0), (0.5, 0.5), (0.1, 3), (-0.1, 0.4), (0.3, 0.1), (1.3,0.12)]
        tsp = TSP(points)

        star = AStarTSP(tsp)
        brute = BruteTSP(tsp)

        result_star = star.solve()
        result_brute = brute.solve()

        self.assertListEqual(result_star, result_brute)


    def test_correct_solve_5(self):
        points = [(1, 0), (0.5, 0.5), (-0.1, 0.4), (0.1, 3), (0.3, 0.1), (0, 0), (1.3,0.12)]
        tsp = TSP(points)

        star = AStarTSP(tsp)
        brute = BruteTSP(tsp)

        result_star = star.solve()
        result_brute = brute.solve()

        self.assertListEqual(result_star, result_brute)