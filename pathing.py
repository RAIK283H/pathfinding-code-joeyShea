import graph_data
import global_game_data
from numpy import random

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
    


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
