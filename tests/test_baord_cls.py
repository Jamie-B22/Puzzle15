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


if __name__ == '__main__':
    unittest.main()