import unittest
from lib.tsp import TSP
from lib.brute_tsp import BruteTSP
from lib.graphical_tsp import GraphicalTSP


class BruteTSPTests(unittest.TestCase):

    def test_correct_solve_1(self):

        points = [(1,1), (2,2), (3,3)]
        nodes = "1 ( 1 1 )\n2 ( 2 2 )\n3 ( 3 3 )"
        links = "Link1 ( 1 2 )\nLink1 ( 2 3 )\nLink1 ( 1 3 )"

        graphical_tsp = GraphicalTSP(nodes, links)

        problem = TSP(graphical_tsp)

        brute = BruteTSP(problem)

        result = brute.solve()

        self.assertListEqual(result[0], points)