from lib.BruteTravelingSalesman import BruteTSP
from lib.tsp import TSP

if __name__ == '__main__':
    # points map is initiates like this and we only need one copy of it
    tsp = TSP(points=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    brute = BruteTSP(tsp)
    print(brute.solve())
