from lib.brute_tsp import BruteTSP
from lib.astar_tsp_solver import AStarTSPSolver
from lib.min_vertex_heuristic_state import MinVertexHeuristicState
from lib.all_min_distance_state import AllMinHeuristicState
from lib.mean_distance_state import MeanDistanceState
from lib.tsp import TSP
import random
import time
import sys


def random_points(number_of_points):
    random.seed(42)
    return [(random.randint(1, 1000), random.randint(1, 1000)) for _ in range(number_of_points)]


def time_function(function, repeat=1):
    start = time.time()
    for _ in range(repeat):
        a = function()
    end = time.time()

    return (end - start) / repeat, a[1], a[2]


def main():
    tsp = TSP(random_points(int(sys.argv[1])))
    brute = BruteTSP(tsp)
    astar = AStarTSPSolver(tsp)

    time_brute = time_function(lambda: brute.solve())
    time_astar_zero_heuristic = time_function(
        lambda: astar.solve())
    time_astar_min_vertex_heuristic = time_function(
        lambda: astar.solve(MinVertexHeuristicState))
    time_astar_all_min_heuristic = time_function(
        lambda: astar.solve(AllMinHeuristicState))
    time_astar_mean_heuristic = time_function(
        lambda: astar.solve(MeanDistanceState))

    print(f'Brute:                     {time_brute} ')
    print(f'Astar zero heuristic:      {time_astar_zero_heuristic}')
    print(f'Astar min from vertex:     {time_astar_min_vertex_heuristic}')
    print(f'Astar all min from vertex: {time_astar_all_min_heuristic}')
    print(f'Astar mean:                {time_astar_mean_heuristic}')


if __name__ == '__main__':
    main()
