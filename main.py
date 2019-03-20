from src.BruteTravelingSalesman import BruteTS
from lib.Map import Map

if __name__ == '__main__':
    # points map is initiates like this and we only need one copy of it
    points_map = Map(points=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    brute = BruteTS(points_map)
    print(brute.compute_shortest_path())
