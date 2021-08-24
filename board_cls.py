"""
    Author: Jamie Bamforth
    Class to create puzzle board instances.
"""
import numpy as np

class SquarePuzzleBoard:


    def __init__(self, n):
        """
        Build board with squares in a random solvable starting position
        :param n: board side length in squares
        :return:
        """
        self.n = n
        self.square_positions = self.starting_board()

    def starting_board(self) -> np.array:
        """
        Randomly initialise a solvable board. The initialisation is done through random moves from a solved board to
        ensure a solution exists as only half of all permutations are solvable
        (see https://en.wikipedia.org/wiki/15_puzzle for more info on this)
        :return square_positions: numpy array of randomly initialised board
        """
        square_positions = np.array([i for i in range(1, self.n**2)] + [0]).reshape((self.n,-1))
        # TODO: randomly shuffle
        return square_positions

    def move(self, square, move):
        pass

    def check_move_valid(self):
        pass

    def valid_moves(self):
        pass

    def check_board_solved(self):
        pass

    def present_board(self):
        pass

if __name__ == '__main__':
    board = SquarePuzzleBoard(4)
    print(board.square_positions)
