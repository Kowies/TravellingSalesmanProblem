import unittest
from lib.tsp import TSP
from lib.astar_tsp_solver import AStarTSPSolver


class AStarTSPTest(unittest.TestCase):
    def setUp(self):
        self.points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        self.tsp = TSP(points=self.points)

    def test_correct_solve(self):
        astar = AStarTSPSolver(self.tsp)

        result = astar.solve()

        self.assertListEqual(result[0], self.points)

    # def test_correct_solve_2(self):
    #     astar = AStarTSPSolver(self.tsp)

    #     result = astar.solve()

    #     self.assertListEqual(result, self.points)
