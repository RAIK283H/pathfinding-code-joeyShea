import graph_data
import global_game_data
from numpy import random
from collections import deque

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
    stack = [(start, [start])]  # Stack holds (current_node, path_to_current_node)
    visited = set()
    
    while stack:
        (current_node, path) = stack.pop()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # If we reach the target, return the path
        if current_node == target:
            return path
        
        # Add neighbors to the stack
        for neighbor in sorted(graph[current_node][1]):  # Assuming graph[node] -> (value, [neighbors])
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return None  # Return None if no path is found

def get_dfs_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(current_graph) > 1, "Graph must have at least a start and exit node"

    start_node = 0
    exit_node = len(current_graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    
    path_to_target = dfs(current_graph, start_node, target_node)
    path_from_target_to_exit = dfs(current_graph, target_node, exit_node)[1:]
    final_path = path_to_target + path_from_target_to_exit

    # Ensure path validation and update scoreboard
    assert final_path[0] == start_node, "Path must start at start node"
    assert final_path[-1] == exit_node, "Path must end at exit node"
    assert target_node in final_path, "Path must reach target node"
    for i in range(len(final_path)):
        assert (final_path[i - 1]) in current_graph[final_path[i]][1] or (final_path[i + 1]) in current_graph[final_path[i]][1], "No edge connects consecutive nodes"

    return final_path


def bfs(graph, start, target):
    queue = deque([(start, [start])])  # Queue holds (current_node, path_to_current_node)
    visited = set()
    
    while queue:
        (current_node, path) = queue.popleft()  # Dequeue the front of the queue
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # If we reach the target, return the path
        if current_node == target:
            return path
        
        # Add neighbors to the queue
        for neighbor in sorted(graph[current_node][1]):  # Assuming graph[node] -> (value, [neighbors])
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Return None if no path is found

def get_bfs_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(current_graph) > 1, "Graph must have at least a start and exit node"

    start_node = 0
    exit_node = len(current_graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    
    path_to_target = bfs(current_graph, start_node, target_node)
    path_from_target_to_exit = bfs(current_graph, target_node, exit_node)[1:]
    final_path = path_to_target + path_from_target_to_exit

    # Ensure path validation and update scoreboard
    assert final_path[0] == start_node, "Path must start at start node"
    assert final_path[-1] == exit_node, "Path must end at exit node"
    assert target_node in final_path, "Path must reach target node"
    for i in range(len(final_path)):
        assert (final_path[i - 1]) in current_graph[final_path[i]][1] or (final_path[i + 1]) in current_graph[final_path[i]][1], "No edge connects consecutive nodes"
    
    return final_path


def get_dijkstra_path():
    return [1,2]
