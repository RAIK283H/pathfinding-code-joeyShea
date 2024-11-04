import math
import unittest
import global_game_data
import pathing
import graph_data
from permutation import find_hamiltonian_cycles, is_hamiltonian_cycle, calculate_distance, get_shortest, SJT

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_random_algorithm(self):
        global_game_data.current_graph_index = 0
        global_game_data.current_player_index = 1
        global_game_data.target_node = [1]
        
        path = pathing.get_random_path()

        self.assertIn(global_game_data.target_node[global_game_data.current_graph_index], path)

    def test_random_algorithm_with_two(self):
        global_game_data.current_graph_index = 1
        global_game_data.current_player_index = 1
        global_game_data.target_node = [1, 1]
        
        path = pathing.get_random_path()

        self.assertIn(global_game_data.target_node[global_game_data.current_graph_index], path)

class TestDFS(unittest.TestCase):
    def setUp(self):
        self.graph = {
            0: ('start', [1, 2]),
            1: ('node1', [0, 3, 4]),
            2: ('node2', [0, 5]),
            3: ('node3', [1]),
            4: ('node4', [1]),
            5: ('node5', [2])
        }
    def test_dfs_direct_path(self):
        path = pathing.dfs(self.graph, 0, 3)
        self.assertEqual(path, [0, 1, 3])
    def test_dfs_no_path(self):
        path = pathing.dfs(self.graph, 0, 6)
        self.assertIsNone(path)
    def test_dfs_longer_path(self):
        path = pathing.dfs(self.graph, 0, 5)
        self.assertEqual(path, [0, 2, 5])

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.graph = {
            0: ('start', [1, 2]),
            1: ('node1', [0, 3, 4]),
            2: ('node2', [0, 5]),
            3: ('node3', [1]),
            4: ('node4', [1]),
            5: ('node5', [2])
        }
    def test_bfs_direct_path(self):
        path = pathing.bfs(self.graph, 0, 3)
        self.assertEqual(path, [0, 1, 3])
    def test_bfs_no_path(self):
        path = pathing.bfs(self.graph, 0, 6)
        self.assertIsNone(path)
    def test_bfs_shortest_path(self):
        path = pathing.bfs(self.graph, 0, 5)
        self.assertEqual(path, [0, 2, 5])

class TestSJTAlgorithm(unittest.TestCase):
    def test_sjt_small_n(self):
        # Test with n = 3 (should generate permutations of [1, 2])
        result = SJT(3)
        expected_permutations = [
            [1, 2, 1],
            [2, 1, 2],
        ]
        self.assertEqual(result, expected_permutations)

    def test_sjt_n_equals_4(self):
        # Test with n = 4 (should generate permutations of [1, 2, 3])
        result = SJT(4)
        expected_length = 6  # 3! permutations of [1, 2, 3]
        self.assertEqual(len(result), expected_length)

        # Check for specific permutations
        self.assertIn([1, 2, 3, 1], result)
        self.assertIn([2, 1, 3, 2], result)

    def test_sjt_n_equals_5(self):
        # Test with n = 5 (should generate permutations of [1, 2, 3, 4])
        result = SJT(5)
        expected_length = 24  # 4! permutations of [1, 2, 3, 4]

        self.assertEqual(len(result), expected_length)

        # Check for some specific permutations
        self.assertIn([1, 2, 3, 4, 1], result)
        self.assertIn([4, 3, 2, 1, 4], result)

    def test_sjt_no_duplicates(self):
        # Test with n = 3 to check for duplicates
        result = SJT(3)

        # Create a set of unique permutations
        unique_permutations = set(tuple(perm) for perm in result)

        # Check if the length matches the original result
        self.assertEqual(len(result), len(unique_permutations))

    def test_sjt_empty_input(self):
        # Test with n = 1 (invalid graph)
        result = SJT(1)
        expected = [-1]  # Invalid graph
        self.assertEqual(result, expected)

class TestHamiltonianCycles(unittest.TestCase):
    def test_no_cycle_graph(self):
        # Graph without a Hamiltonian cycle
        graph = [
            [(0, 0), [1]],  # start node
            [(100, -100), [2]],
            [(200, -200), [1, 3]],
            [(200, -400), [2]],
            [(300, -500), []]  # end node
        ]
        self.assertEqual(find_hamiltonian_cycles(graph), [-1])

    def test_no_cycle_graph_complex(self):
        # Graph without a Hamiltonian cycle
        graph = [
            [(0, 0), [1]],  # start node
            [(50, -200), [2]],
            [(100, -300), [1, 3]],
            [(150, -500), [2, 4]],
            [(200, -600), []]  # end node
        ]
        self.assertEqual(find_hamiltonian_cycles(graph), [-1])

    def test_has_cycle_graph_simple(self):
        # Simple cycle graph (expecting Hamiltonian cycles)
        graph = [
            [(-200, -200), [1]],  # start node
            [(-100, -100), [2, 3, 4]],
            [(0, 0), [1, 3, 5]],
            [(50, 50), [1, 2, 4, 5]],
            [(100, 100), [1, 3, 5, 6]],
            [(150, 50), [2, 4, 6]],
            [(200, 0), [5, 7]],
            [(300, 300), []]  # end node
        ]
        cycles = find_hamiltonian_cycles(graph)
        self.assertNotEqual(cycles, [-1])
        self.assertTrue(all(is_hamiltonian_cycle(c, graph) for c in cycles))

    def test_has_cycle_graph_complex(self):
        # Complex cycle graph (expecting Hamiltonian cycles)
        graph = [
            [(-300, -300), [1]],  # start node
            [(-200, -200), [2, 3]],
            [(0, 0), [1, 3, 4]],
            [(100, 0), [1, 2, 4, 5]],
            [(200, 0), [2, 3, 6]],
            [(300, 100), [3, 6, 7]],
            [(400, 400), [5, 8]],
            [(500, 500), []]  # end node
        ]
        cycles = find_hamiltonian_cycles(graph)
        self.assertNotEqual(cycles, [-1])
        self.assertTrue(all(is_hamiltonian_cycle(c, graph) for c in cycles))

    def test_disconnected_graph(self):
        # Graph with no Hamiltonian cycles due to disconnection
        graph = [
            [(-300, -300), [1]],  # start node
            [(-200, -200), [2, 3]],
            [(0, 0), [1]],
            [(50, 50), [1, 4]],
            [(100, 100), [3, 5]],
            [(150, 150), [4, 6]],
            [(200, 200), []]  # end node
        ]
        self.assertEqual(find_hamiltonian_cycles(graph), [-1])

    def test_shortest_cycle(self):
        # Test if get_shortest function finds the shortest Hamiltonian cycle
        graph = [
            [(-400, -400), [1]],  # start node
            [(-300, -300), [2, 3]],
            [(0, 0), [1, 4]],
            [(100, 0), [1, 4, 5]],
            [(200, 0), [2, 3, 6]],
            [(300, 100), [3, 6]],
            [(400, 400), [4, 7]],
            [(500, 500), []]  # end node
        ]
        cycles = find_hamiltonian_cycles(graph)
        shortest_cycle = get_shortest(graph, cycles)
        self.assertIsNotNone(shortest_cycle)  # Ensure a shortest cycle is found
        self.assertTrue(is_hamiltonian_cycle(shortest_cycle, graph))


if __name__ == '__main__':
    unittest.main()
