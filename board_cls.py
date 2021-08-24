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
        self.max_char_len = len(str(self.square_positions.max()))

    def starting_board(self) -> np.array:
        """
        Randomly initialise a solvable board. The initialisation is done through random moves from a solved board to
        ensure a solution exists as only half of all permutations are solvable
        (see https://en.wikipedia.org/wiki/15_puzzle for more info on this)
        :return square_positions: numpy array of randomly initialised board
        """
        square_positions = np.array([i for i in range(1, self.n**2)] + [0]).reshape((self.n,-1))
        # square_positions = np.array([i for i in range(1, self.n + 1)] + [0] + [i for i in range(self.n + 1, self.n**2)]).reshape((self.n, -1))
        # TODO: randomly shuffle
        return square_positions

    def move(self, square, move):
        pass

    def check_move_valid(self):
        pass

    def valid_moves(self) -> list:
        """
        Returns a list of valis moves, each move a tuple of format (row, column, direction)
        :return valid_moves: a list of valid moves
        """
        empty_row, empty_col = [i[0] for i in np.where(self.square_positions == 0)]
        valid_moves = []
        if empty_row > 0:
            down_move = (empty_row - 1, empty_col, 'd')
            valid_moves.append(down_move)
        if empty_row < self.n - 1:
            up_move = (empty_row + 1, empty_col, 'u')
            valid_moves.append(up_move)
        if empty_col > 0:
            right_move = (empty_row, empty_col - 1, 'r')
            valid_moves.append(right_move)
        if empty_col < self.n - 1:
            left_move = (empty_row, empty_col + 1, 'l')
            valid_moves.append(left_move)

        return valid_moves

    def check_board_solved(self):
        pass

    def present_board(self):
        board_str = ''
        board_str += ' ' + (self.max_char_len + 3) * self.n * '-' + '-\n'
        for i in range(self.n):
            for j in range(self.n):
                board_str += ' | ' + str(self.square_positions[i,j]).rjust(self.max_char_len)
            board_str += ' |\n'
            board_str += ' ' + (self.max_char_len + 3)* self.n * '-' + '-\n'
        print(board_str)

    def move_input_checker(self):
        pass

if __name__ == '__main__':
    board = SquarePuzzleBoard(4)
    print(board.square_positions)
    print(board.valid_moves())
    print(board.max_char_len)
    board.present_board()
