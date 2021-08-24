import unittest
import numpy as np
from board_cls import SquarePuzzleBoard

class TestSquarePuzzleBoard(unittest.TestCase):
    def test_init(self):
        pass

    def test_valid_moves(self):
        n = 4
        board = SquarePuzzleBoard(n)
        board.square_positions = np.array([i for i in range(1, n + 1)] + [0] + [i for i in range(n + 1, n**2)]).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(0, 0, 'd'), (2, 0, 'u'), (1, 1, 'l')])

        board.square_positions = np.array([i for i in range(1, n)] + [0] + [i for i in range(n, n ** 2)]).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(1, 3, 'u'), (0, 2, 'r')])

        board.square_positions = np.array([i for i in range(1, n+2)] + [0] + [i for i in range(n+2, n ** 2)]).reshape(
            (n, -1))
        self.assertEqual(board.valid_moves(), [(0, 1, 'd'), (2, 1, 'u'), (1, 0, 'r'), (1, 2, 'l')])

    def test_create_solution_board(self):
        for n in [2,3,4,5,6,10,178]:
            solution = np.array([i for i in range(1, n ** 2)] + [0]).reshape((n, -1))
            board = SquarePuzzleBoard(n)
            self.assertTrue(np.all(board.solution_board == solution))

    def test_check_board_solved_true(self):
        for n in [2,3,4,267,9]:
            solution = np.array([i for i in range(1, n ** 2)] + [0]).reshape((n, -1))
            board = SquarePuzzleBoard(n)
            board.square_positions = solution
            self.assertTrue(board.check_board_solved())

    def test_check_board_solved_false(self):
        for n in [2,3,4,5,6,10,178]:
            not_solution = np.array([i for i in range(1, n + 1)] + [0] + [i for i in range(n + 1, n**2)]).reshape((n, -1))
            board = SquarePuzzleBoard(n)
            board.square_positions = not_solution
            self.assertFalse(board.check_board_solved())


if __name__ == '__main__':
    unittest.main()