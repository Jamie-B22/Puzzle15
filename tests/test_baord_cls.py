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
        self.assertEqual(board.valid_moves(), [(0, 0), (2, 0), (1, 1)])

        board.square_positions = np.array([i for i in range(1, n)] + [0] + [i for i in range(n, n ** 2)]).reshape((n, -1))
        self.assertEqual(board.valid_moves(), [(1, 3), (0, 2)])

        board.square_positions = np.array([i for i in range(1, n+2)] + [0] + [i for i in range(n+2, n ** 2)]).reshape(
            (n, -1))
        self.assertEqual(board.valid_moves(), [(0, 1), (2, 1), (1, 0), (1, 2)])

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

    def test_move_valid_move(self):
        n = 4
        board = SquarePuzzleBoard(n)
        board.square_positions = np.array([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 12], [13, 14, 15, 0]])
        board.move((n-2,n-1))
        current_board = np.array([[ 1, 2, 3, 4], [ 5, 6, 7, 8], [ 9, 10, 11, 0], [13, 14, 15, 12]])
        print(board.square_positions)
        board.move((n - 2, n - 1))
        print(board.square_positions)


if __name__ == '__main__':
    unittest.main()