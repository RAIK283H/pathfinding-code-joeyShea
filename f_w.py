import math
from graph_data import graph_data

def create_adj_matrix(graph):
    n = len(graph)
    inf = math.inf
    
    # Initialize the adjacency matrix with infinity and an empty parent matrix
    dist_matrix = [[inf] * n for _ in range(n)]
    parent_matrix = [[None] * n for _ in range(n)]
    
    # Fill the adjacency matrix with actual distances and set up parent pointers
    for node, (coords, neighbors) in enumerate(graph):
        dist_matrix[node][node] = 0
        for neighbor in neighbors:
            neighbor_coords = graph[neighbor][0]
            # Calculate distance
            distance = math.sqrt((coords[0] - neighbor_coords[0]) ** 2 + (coords[1] - neighbor_coords[1]) ** 2)
            dist_matrix[node][neighbor] = distance
            parent_matrix[node][neighbor] = node
    
    return dist_matrix, parent_matrix, n

def floyd_warshall(dist_matrix, parent_matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    parent_matrix[i][j] = k

def reconstruct_path(parent_matrix, start, end):
    path = []
    z = parent_matrix[start][end]
    
    while z is not None:
        path.insert(0, z)
        z = parent_matrix[start][z]
    
    if len(path) > 0:
        path.append(end)
    return path

dist_matrix, parent_matrix, n = create_adj_matrix(graph_data[0])
floyd_warshall(dist_matrix, parent_matrix, n)

start = 0
end = 2
path = reconstruct_path(parent_matrix, start, end)
print(f"Shortest path from {start} to {end}: {path}")
