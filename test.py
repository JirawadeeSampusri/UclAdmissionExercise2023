import unittest

from mat_to_list import mat_to_list
from reachable import reachable


class TestGraphFunctions(unittest.TestCase):

    def setUp(self):
        self.adj_mat = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ]
        self.adj_list = [
            [1],
            [0, 2],
            [1, 3],
            [2]
        ]
        self.start_node = 0

    def test_reachable(self): 
        expected_output = [0, 1, 2, 3]
        self.assertEqual(reachable(self.adj_list, self.start_node), expected_output)

    def test_reachable_1(self):
        expected_output = [0, 2, 3]
        self.assertNotEqual(reachable(self.adj_list, self.start_node), expected_output)

    def test_mat_to_list(self):
        expected_output = self.adj_list
        self.assertEqual(mat_to_list(self.adj_mat), expected_output)

    def test_mat_to_list_1(self):
        expected_output =  [[1],[0, 1],[1, 3],[2]]
        self.assertNotEqual(mat_to_list(self.adj_mat), expected_output)

if __name__ == '__main__':
    unittest.main()