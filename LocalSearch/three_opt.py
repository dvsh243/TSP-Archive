import random
from utils import getPathLength, getPathCoords
import matplotlib.pyplot as plt


def threeOptSwap(path, cities, N=100, visual = False):
    """
    we can't modify 1st and last cities of path
    (path will start at city 0 and end at city 0)
    """
    
    # print(f"og path length -> {getPathLength(path, cities)}\n")
    swapCount = 0
    minTour = getPathLength(path, cities)

    if visual: 
        xpath, ypath = getPathCoords(path, cities)


    for i in range(N):
        if visual:
            plt.scatter(xpath, ypath)
            plt.suptitle(f" 3 Opt ({i} swap) - {minTour} km")
            for i in range(len(cities)): plt.annotate(i, (xpath[i], ypath[i]))
            xpath, ypath = getPathCoords(path, cities)
            plt.plot(xpath, ypath)
            plt.pause(0.01)
            plt.clf()
        else:
            if i % 100 == 0: print(f"{str((i / N) * 100)[:10]}% swaps done.", end='\r')

        newPath = swapCities(path, cities)
        # print(f"new path length -> {getPathLength(newPath, cities)}")

        if getPathLength(newPath, cities) < minTour:
            minTour = getPathLength(newPath, cities)
            path = newPath
            swapCount += 1

    print(f"Swapped {swapCount} / {N} times to find optimal solution.")
    return minTour, path



def swapCities(path, cities):
    newPath = path.copy()
    
    u = random.randint(1, len(cities)-1)
    v = random.randint(1, len(cities)-1)
    w = random.randint(1, len(cities)-1)
    while u == v:
        v = random.randint(1, len(cities)-1)
    while w == u or w == v:
        w = random.randint(1, len(cities)-1)
    
    # print(f"two cities to swap -- ({path[u]}) <-> ({path[v]})")
    newPath[v], newPath[u], newPath[w] = path[u], path[w], path[v]
    # v -> u, u -> w, w -> v

    return newPath