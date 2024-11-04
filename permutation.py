import math

'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''
graph_data = [

    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
    ],
    [ #Should have cycles
        [(-100, -100), [1]], # start
        [(0, 0), [0, 2, 3, 4]],
        [(0, 100), [1, 3, 5]],
        [(50, 50), [1, 2, 4, 5]],
        [(100, 0), [1, 3, 5, 6]],
        [(100, 100), [2, 3, 4, 6]],
        [(150, 50), [4, 5, 7]],
        [(400, 400), [6]], # end
    ],
    [ #Should have cycles
        [(-100, -100), [1]], # start
        [(0, 0), [0, 2, 4]],
        [(100, 0), [1, 3, 4, 5]],
        [(200, 0), [2, 5]],
        [(0, 100), [1, 2, 5]],
        [(200, 100), [2, 3, 4, 6]],
        [(400, 400), [5]], # end
    ],
    [ #Should NOT have cycles
        [(-100, -100), [1]], # start
        [(0, 50), [2, 3, 4]],
        [(50, 0), [1, 5]],
        [(50, 50), [1, 5]],
        [(50, 100), [1, 5]],
        [(100, 50), [2, 4]],
        [(200, 200), [5]], # end
    ]
]

def SJT(n):
    # 1. Initialize list of ordered integers with directions pointing left (from 1 to n-1, -1 = left, +1 = right)
    sequence = list(range(1, n))
    directions = [-1] * (n - 1)

    # Graph must have at least a start node, end node, and one other to have a hamiltonian cycle within it
    if n < 2:
        return [-1]
    
    # 2. Find largest mobile integer
    def find_largest_mobile_integer():
        index = -1

        for i in range(n - 1):
            mobile_left = directions[i] == -1 and i > 0 and sequence[i] > sequence[i - 1]
            mobile_right = directions[i] == 1 and i < n - 2 and sequence[i] > sequence[i + 1]

            if (mobile_left or mobile_right):
                if index == -1 or sequence[i] > sequence[index]:
                    index = i
        return index

    result = [sequence[:] + [sequence[0]]]
    while True:
        mobile_index = find_largest_mobile_integer()
        if mobile_index == -1:
            break  # All permutations have been generated

        # 3. Swap largest mobile integer with neighbor it points to
        direction = directions[mobile_index]
        swap_index = mobile_index + direction
        sequence[mobile_index], sequence[swap_index] = sequence[swap_index], sequence[mobile_index]
        directions[mobile_index], directions[swap_index] = directions[swap_index], directions[mobile_index]

        # 4. Switch direction of all integers with values greater than mobile integer
        largest_mobile = sequence[swap_index]
        for i in range(n - 1):
            if sequence[i] > largest_mobile:
                directions[i] = -directions[i]

        result.append(sequence[:] + [sequence[0]])

    return result

def is_hamiltonian_cycle(permutations, graph):
    start_node = 1
    
    if permutations[0] != start_node or permutations[-1] != start_node:
        return False
    
    # Check adjacency for each consecutive pair
    if (len(permutations) > 2):
        for i in range(len(permutations) - 1):
            current_node = permutations[i]
            next_node = permutations[i + 1]
            if next_node not in graph[current_node][1]:
                return False
    
    return True

def find_hamiltonian_cycles(graph):
    hamiltonian_cycles = []
    n = len(graph) - 1
    permutations = SJT(n)
    
    # Check each permutation
    for perm in permutations:
        if is_hamiltonian_cycle(perm, graph):
            hamiltonian_cycles.append(perm)
    
    if len(hamiltonian_cycles) > 0:
        return hamiltonian_cycles
    else:
        return [-1]

def calculate_distance(graph, node_a, node_b):
    x1, y1 = graph[node_a][0]
    x2, y2 = graph[node_b][0]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_shortest(graph, cycles):
    shortest_distance = float('inf')
    shortest_cycle = None

    for cycle in cycles:
        total_distance = sum(calculate_distance(graph, cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1))
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_cycle = cycle

    # Display the result
    print("The shortest cycle is:", shortest_cycle)
    print("With a total distance of:", shortest_distance)
    return shortest_cycle


if __name__ == '__main__':
    for graph in graph_data:
        cycles = find_hamiltonian_cycles(graph)

        print("Valid Hamiltonian Cycles:")
        for i in cycles:
            print(i)
        if (cycles != [-1]):
            get_shortest(graph, cycles)
        print()