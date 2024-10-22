import math
import unittest
import global_game_data
import pathing
import graph_data


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

if __name__ == '__main__':
    unittest.main()
