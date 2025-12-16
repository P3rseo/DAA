# Python program to find closet point
import math


# Function to compute Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Function that returns the smallest distance
# between any pair of points
def minDistance(points):
    n = len(points)

    minDist = float('inf')

    # Brute force to check all pairs
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < minDist:
                minDist = dist

    # Return the smallest distance
    return minDist


if __name__ == "__main__":
    points = [[-1, -2], [0, 0], [1, 2], [2, 3]]

    res = minDistance(points)

    print(f"{res:.6f}")