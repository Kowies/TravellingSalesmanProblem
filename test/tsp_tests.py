import unittest
from lib.tsp import euclidean_distance, TSP
from lib.graphical_tsp import GraphicalTSP


class DistanceTests(unittest.TestCase):
    def test_euklidean_distance_1(self):
        p1 = (1, 2)
        p2 = (2, 2)
        self.assertEqual(euclidean_distance(p1, p2), 1)


class TSPTests(unittest.TestCase):
    def test_map(self):
        
        nodes = "1 ( 1 1 )\n2 ( 1 2 )\n3 ( 3 3 )\n4 ( 4 4 )"
        links = "Link1 ( 1 2 )"
        graphical_tsp = GraphicalTSP(nodes, links)

        problem = TSP(graphical_tsp)

        self.assertEqual(problem.distance(0, 1), 1)

        self.assertEqual(problem.get_points_count(), 4)

        self.assertEqual(problem.get_point(2), (3, 3) )



if __name__ == '__main__':
    unittest.main()
