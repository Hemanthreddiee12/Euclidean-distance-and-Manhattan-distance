import math

def euc_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same dimension")
    
    distance = 0.0
    for i in range(len(vec1)):
        distance += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(distance)


def man_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be of the same dimension")
    
    distance = 0.0
    for i in range(len(vec1)):
        distance += abs(vec1[i] - vec2[i])
    return distance


if __name__ == "__main__":
    # enter elements of the vectors
    vector_size = int(input("Enter the size of vectors: "))
    print("Enter elements of vector 1:")
    vec1 = [float(input()) for _ in range(vector_size)]
    print("Enter elements of vector 2:")
    vec2 = [float(input()) for _ in range(vector_size)]
    
    # Calculating distances
    euclidean_dist = euc_distance(vec1, vec2)
    manhattan_dist = man_distance(vec1, vec2)
    
    # Printing distances
    print("Euclidean Distance:", euclidean_dist)
    print("Manhattan Distance:", manhattan_dist)
