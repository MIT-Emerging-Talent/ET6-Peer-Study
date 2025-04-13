# Define a weighted, undirected graph using an adjacency dictionary
graph = { 
    0: {1: 6, 2: 4, 3: 2, 4: 3},
    1: {0: 6, 2: 6, 3: 2, 4: 2},
    2: {0: 4, 1: 6, 3: 8, 4: 2},
    3: {0: 2, 1: 2, 2: 8, 4: 4},
    4: {0: 3, 1: 2, 2: 2, 3: 4} 
}


def get_all_paths(graph, start, end, path=[]):
    """
    Recursively find all possible paths from a starting node to an ending node in a graph.

    Parameters:
        graph (dict): The adjacency list representation of the graph where each node maps 
                      to a dictionary of its neighbors and the edge weights.
        start (int): The starting node in the path.
        end (int): The destination node where the path should end.
        path (list): The current path being explored (used for recursion and backtracking).

    Returns:
        list of lists: A list containing all possible paths from start to end.
                       Each path is represented as a list of nodes.
    """
    path = path + [start]  # Create a new path list that includes the current node

    # Base case: if the current node is the destination, return the completed path
    if start == end:
        return [path]

    paths = []  # List to store all valid paths from start to end

    # Recur for each neighbor not already in the path (to avoid cycles)
    for neighbor in graph[start]:
        if neighbor not in path:
            newPaths = get_all_paths(graph, neighbor, end, path)
            for p in newPaths:
                paths.append(p)

    return paths


def calculate_path_weight(graph, path):
    """
    Calculate the total weight (cost) of a given path in a weighted graph.

    Parameters:
        graph (dict): The adjacency list of the graph where each edge has a weight.
        path (list): A list of node indices representing a path in the graph.

    Returns:
        int: The total sum of the weights of all consecutive edges in the path.
    """
    weight = 0

    # Sum the weight of each edge in the path
    for i in range(len(path) - 1):
        weight += graph[path[i]][path[i + 1]]

    return weight


def brute_force_shortest_path(graph, start, end):
    """
    Use brute-force approach to find the shortest path between two nodes
    by evaluating all possible paths and selecting the one with the least total weight.

    Parameters:
        graph (dict): The weighted graph represented as an adjacency dictionary.
        start (int): The starting node for the path.
        end (int): The target node to reach.

    Returns:
        tuple: A tuple containing:
            - min_path (list): The path with the minimum total weight.
            - min_weight (int): The total weight of that shortest path.
    """
    all_paths = get_all_paths(graph, start, end)  # Get all paths from start to end

    min_path = None
    min_weight = float("inf")  # Initialize with infinity for comparison

    # Evaluate the weight of each path and keep track of the minimum
    for path in all_paths:
        weight = calculate_path_weight(graph, path)
        if weight < min_weight:
            min_weight = weight
            min_path = path  # Update shortest path if current one is lighter

    return (min_path, min_weight)


# Example usage: Find the shortest path from node 3 to node 1
print(brute_force_shortest_path(graph, 3, 1))