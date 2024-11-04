import graph_data

def SJT(n):
    # 1. Initialize list of ordered integers with directions pointing left (from 1 to n-1, -1 = left, +1 = right)
    sequence = list(range(1, n))
    directions = [-1] * (n - 1)

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

def find_hamiltonian_cycles(graph_data):
    hamiltonian_cycles = []
    for graph in graph_data:
        n = len(graph) - 1
        permutations = SJT(n)
        
        # Check each permutation
        for perm in permutations:
            if is_hamiltonian_cycle(perm, graph):
                hamiltonian_cycles.append(perm)
                
    return hamiltonian_cycles

if __name__ == '__main__':
    graph = [[
    [(0, 300), [1]],
    [(100, 300), [0, 2, 3, 4, 5, 6, 7, 8]],
    [(300, 100), [1, 3, 4, 5, 6, 7, 8]],
    [(500, 300), [1, 2, 4, 5, 6, 7, 8, 9]],
    [(300, 500), [1, 2, 3, 5, 6, 7, 8]],
    [(200, 200), [1, 2, 3, 4, 6, 7, 8]],
    [(400, 200), [1, 2, 3, 4, 5, 7, 8]],
    [(200, 400), [1, 2, 3, 4, 5, 6, 8]],
    [(400, 400), [1, 2, 3, 4, 5, 6, 7]],
    [(600, 300), [3]],
    ]]
    
    #graphs = graph_data.graph_data
    cycles = find_hamiltonian_cycles(graph)

    print(len(cycles))