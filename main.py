from lib.graphical_tsp import GraphicalTSP
from lib.brute_tsp import BruteTSP
from lib.astar_tsp_solver import AStarTSPSolver
from lib.min_vertex_heuristic_state import MinVertexHeuristicState
from lib.all_min_distance_state import AllMinHeuristicState
from lib.mean_distance_state import MeanDistanceState
from lib.tsp import TSP
from lib.graphical_tsp import GraphicalTSP

import random
import time
import sys


def time_function(function, repeat=1):
    start = time.time()
    for _ in range(repeat):
        a = function()
    end = time.time()
    return (end - start) / repeat, a[1], a[2], a[0]

# NodesNorway.txt , LinksNorway.txt
# NodesPoland.txt , LinksPoland.txt
# NodesSmall.txt , LinksSmall.txt
# NodesEU.txt , LinksEU.txt


def main():
    with open("data/NodesNorway.txt") as f:
        nodes = f.read()

    with open("data/LinksNorway.txt") as f:
        links = f.read()

    graphical_tsp = GraphicalTSP(nodes, links)
    tsp = TSP(graphical_tsp)

    brute = BruteTSP(tsp)
    astar = AStarTSPSolver(tsp)

    time_brute = time_function(lambda: brute.solve())
    print(f'Brute:                     {time_brute} ')

    time_astar_min_vertex_heuristic = time_function(
        lambda: astar.solve(MinVertexHeuristicState))
    print(f'Astar min from vertex:     {time_astar_min_vertex_heuristic}')

    time_astar_mean_heuristic = time_function(
        lambda: astar.solve(MeanDistanceState))
    print(f'Astar mean:                {time_astar_mean_heuristic}')

    time_astar_all_min_heuristic = time_function(
        lambda: astar.solve(AllMinHeuristicState))
    print(f'Astar all min from vertex: {time_astar_all_min_heuristic}')

    time_astar_zero_heuristic = time_function(
        lambda: astar.solve())
    print(f'Astar zero heuristic:      {time_astar_zero_heuristic}')


if __name__ == '__main__':
    main()
