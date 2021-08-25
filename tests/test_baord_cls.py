"""
    Author: Jamie Bamforth
    Tests code in board_cls.py
"""

import unittest
import numpy as np
import random
from classes.board_cls import PuzzleBoard


class TestSquarePuzzleBoard(unittest.TestCase):
    def test_init(self):
        for n in [3, 4, 5, 6, 100, 238]:
            m = random.randint(1, 2 * n)
            board = PuzzleBoard(n, m, 2 * n)
            self.assertEqual(board.rows, n)
            self.assertEqual(board.cols, m)
            self.assertEqual(board._num_shuffle_moves, 2 * n)
            self.assertEqual(board._solution_board.shape, (n, m))
            self.assertEqual(board._max_char_len, len(str(n * m - 1)))
            self.assertEqual(board._square_positions.shape, (n, m))

    def test_valid_moves(self):
        n = 4
        m = n
        board = PuzzleBoard(n, m)
        board._square_positions = np.array(
            [i for i in range(1, n + 1)] + [0] + [i for i in range(n + 1, n ** 2)]
        ).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(0, 0), (2, 0), (1, 1)])

        board._square_positions = np.array(
            [i for i in range(1, n)] + [0] + [i for i in range(n, n ** 2)]
        ).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(1, 3), (0, 2)])

        board._square_positions = np.array(
            [i for i in range(1, n + 2)] + [0] + [i for i in range(n + 2, n ** 2)]
        ).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(0, 1), (2, 1), (1, 0), (1, 2)])

    def test_create_solution_board(self):
        for n in [2, 3, 4, 5, 6, 10, 178]:
            solution = np.array([i for i in range(1, n ** 2)] + [0]).reshape((n, -1))
            board = PuzzleBoard(n, n)
            self.assertTrue(np.all(board._solution_board == solution))

    def test_check_board_solved_true(self):
        for n in [2, 3, 4, 267, 9]:
            solution = np.array([i for i in range(1, n ** 2)] + [0]).reshape((n, -1))
            board = PuzzleBoard(n, n)
            board._square_positions = solution
            self.assertTrue(board.check_board_solved())

    def test_check_board_solved_false(self):
        for n in [2, 3, 4, 5, 6, 10, 178]:
            not_solution = np.array(
                [i for i in range(1, n + 1)] + [0] + [i for i in range(n + 1, n ** 2)]
            ).reshape((n, -1))
            board = PuzzleBoard(n, n)
            board._square_positions = not_solution
            self.assertFalse(board.check_board_solved())

    def test_make_move(self):
        n = 4
        m = n
        board = PuzzleBoard(n, m)
        board._square_positions = np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        )
        board.make_move((n - 2, n - 1))
        # valid move, board should have moved
        current_board = np.array(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]]
        )
        self.assertTrue(np.all(board._square_positions == current_board))
        board.make_move((n - 2, n - 1))
        # invalid move, board should not have moved
        self.assertTrue(np.all(board._square_positions == current_board))


if __name__ == "__main__":
    unittest.main()
