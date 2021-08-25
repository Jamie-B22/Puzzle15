"""
    Author: Jamie Bamforth
    Class to create puzzle board instances.
"""
import numpy as np
import random


class PuzzleBoard:
    """
    Note that 0 is used to indicate the blank square
    """

    def __init__(self, rows: int, cols: int, num_shuffle_moves: int = 100):
        """
        Build board with squares in a random solvable starting position
        :param rows: int, number of board rows
        :param cols: int, number of board columns
        :param num_shuffle_moves: int, number of moves to shuffle initial board by
        :return:
        """
        self.rows = rows
        self.cols = cols
        self._num_shuffle_moves = num_shuffle_moves
        self._solution_board = self.create_solution_board()
        self._max_char_len = len(str(self._solution_board.max()))
        self.create_starting_board()

    def create_solution_board(self) -> np.array:
        """
        Creates an array that is the solution to the board
        :return: n by n dimensional np.array with numbers in order from 1 to n**2 - 1 and the last element being 0 to
                indicate the empty square
        """
        return np.array([i for i in range(1, self.rows * self.cols)] + [0]).reshape(
            (self.rows, -1)
        )

    def create_starting_board(self):
        """
        Randomly initialise a solvable board. The initialisation is done through random moves from a solved board to
        ensure a solution exists as only half of all permutations are solvable
        (see https://en.wikipedia.org/wiki/15_puzzle for more info on this)
        :return square_positions: numpy array of randomly initialised board
        """
        self._square_positions = self._solution_board.copy()
        for _ in range(self._num_shuffle_moves):
            move = random.choice(self.valid_moves())
            self.make_move(move)
        self._board_initialised = True

    def make_move(self, move_tuple: tuple):
        """
        Takes in a tuple of format (row, column) indicating the square that should be moved into the empty space. Checks
        the move is valid and uf so updates the board. Otherwise prints an 'Invalid move' message to the user and leaves
        board as is.
        :param move_tuple:
        :return:
        """
        if move_tuple in self.valid_moves():
            row = move_tuple[0]
            col = move_tuple[1]
            number_moved = self._square_positions[row, col]
            self._square_positions[self._square_positions == 0] = number_moved
            self._square_positions[row, col] = 0

        else:
            print(
                f"\nInvalid move, please choose from these valid squares to move:\n{self.valid_moves()}"
            )

    def valid_moves(self) -> list:
        """
        Returns a list of valid moves, each move a tuple of format (row, column)
        :return valid_moves: a list of valid moves
        """
        empty_row, empty_col = [i[0] for i in np.where(self._square_positions == 0)]
        valid_moves = []
        if empty_row > 0:
            down_move = (empty_row - 1, empty_col)
            valid_moves.append(down_move)
        if empty_row < self.rows - 1:
            up_move = (empty_row + 1, empty_col)
            valid_moves.append(up_move)
        if empty_col > 0:
            right_move = (empty_row, empty_col - 1)
            valid_moves.append(right_move)
        if empty_col < self.cols - 1:
            left_move = (empty_row, empty_col + 1)
            valid_moves.append(left_move)

        return valid_moves

    def check_board_solved(self) -> bool:
        """
        Checks board against solution and returns True if hey are the same. Returns False if different.
        :return:
        """
        return np.all(self._square_positions == self._solution_board)

    def present_board(self):
        """
        Prints a prettily formatted board
        :return:
        """
        board_str = ""
        board_str += " " + (self._max_char_len + 3) * self.cols * "-" + "-\n"
        for i in range(self.rows):
            for j in range(self.cols):
                board_str += " | " + (
                    str(self._square_positions[i, j]).rjust(self._max_char_len)
                    if self._square_positions[i, j] != 0
                    else self._max_char_len * " "
                )
            board_str += " |\n"
            board_str += " " + (self._max_char_len + 3) * self.cols * "-" + "-\n"
        print(board_str)
