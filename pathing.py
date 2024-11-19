import graph_data
import global_game_data
from numpy import random
from collections import deque
import heapq
from math import sqrt

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(current_graph) > 1, "Graph must have at least a start and exit node"

    start_node = 0
    exit_node = len(current_graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    has_visited_target = False
    random_path = [0]

    current_node_index = start_node
    while (not has_visited_target or current_node_index != exit_node):
        current_node = current_graph[current_node_index]
        next_node_index = random.choice(current_node[1])
        
        if has_visited_target or next_node_index != exit_node:
            random_path.append(int(next_node_index))
            current_node_index = next_node_index

        if current_node_index == target_node:
            has_visited_target = True
    
    assert random_path[0] == start_node, "Path must begin with start node"
    assert random_path[len(random_path) - 1] == exit_node, "Path must end with exit node"
    assert target_node in random_path, "Path must reach target node"

    return random_path
    
def dfs(graph, start, target):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        (current_node, path) = stack.pop()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == target:
            return path
        
        for neighbor in sorted(graph[current_node][1]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return None

def get_dfs_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(current_graph) > 1, "Graph must have at least a start and exit node"
    start_node = 0
    exit_node = len(current_graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    
    path_to_target = dfs(current_graph, start_node, target_node)
    path_from_target_to_exit = dfs(current_graph, target_node, exit_node)[1:]
    final_path = path_to_target + path_from_target_to_exit

    assert final_path[0] == start_node, "Path must start at start node"
    assert final_path[-1] == exit_node, "Path must end at exit node"
    assert target_node in final_path, "Path must reach target node"
    for i in range(len(final_path)):
        assert (final_path[i - 1]) in current_graph[final_path[i]][1] or (final_path[i + 1]) in current_graph[final_path[i]][1], "No edge connects consecutive nodes"
    return final_path

def bfs(graph, start, target):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (current_node, path) = queue.popleft()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == target:
            return path
        
        for neighbor in sorted(graph[current_node][1]):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

def get_bfs_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(current_graph) > 1, "Graph must have at least a start and exit node"
    start_node = 0
    exit_node = len(current_graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    
    path_to_target = bfs(current_graph, start_node, target_node)
    path_from_target_to_exit = bfs(current_graph, target_node, exit_node)[1:]
    final_path = path_to_target + path_from_target_to_exit

    assert final_path[0] == start_node, "Path must start at start node"
    assert final_path[-1] == exit_node, "Path must end at exit node"
    assert target_node in final_path, "Path must reach target node"
    for i in range(len(final_path)):
        assert (final_path[i - 1]) in current_graph[final_path[i]][1] or (final_path[i + 1]) in current_graph[final_path[i]][1], "No edge connects consecutive nodes"
    
    return final_path

def dijkstra(graph, start_node, end_node):
    # Priority queue: stores (cost, node, path)
    pq = [(0, start_node, [start_node])]
    visited = set()
    
    while pq:
        cost, current_node, path = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == end_node:
            return path
        
        for neighbor in graph[current_node][1]:
            if neighbor not in visited:
                x1, y1 = graph[current_node][0]
                x2, y2 = graph[neighbor][0]

                distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                heapq.heappush(pq, (cost + distance, neighbor, path + [neighbor]))
    
    return []

def get_dijkstra_path():
    current_player_index = global_game_data.current_player_index
    current_graph_index = global_game_data.current_graph_index
    target_node = global_game_data.target_node
    
    graph = graph_data.graph_data[current_graph_index]
    start_node = 0
    target = target_node[current_player_index] if target_node else len(graph) - 1
    exit_node = len(graph) - 1
    
    path_to_target = dijkstra(graph, start_node, target)
    path_to_exit = dijkstra(graph, target, exit_node)
    
    if path_to_exit and path_to_target:
        full_path = path_to_target[:-1] + path_to_exit
    else:
        full_path = path_to_target + path_to_exit
    
    assert full_path[0] == start_node, "Path does not begin with the start node."
    assert full_path[len(full_path) - 1] == exit_node, "Path does not end with the exit node."
    assert full_path[0] == start_node, "Path does not begin with the start node."
    for i in range(len(full_path)):
        assert (full_path[i - 1]) in graph[full_path[i]][1] or (full_path[i + 1]) in graph[full_path[i]][1], "No edge connects consecutive nodes"

    return full_path