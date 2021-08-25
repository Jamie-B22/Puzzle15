"""
    Author: Jamie Bamforth
    Class for creating a game.
"""


class PuzzleGame:
    def __init__(self, board: object, parser: object):
        """
        Initialise a puzzle game with the relevant board and input parser
        :param board: an instance of the relevant puzzle board
        :param parser: an instance of the parser that interacts with the users input
        """
        self.board = board
        self.parser = parser

    def intro_message(self):
        """
        Prints an intro message and instructions for the user
        :return:
        """
        print(
            f"Welcome to the Puzzle{self.board.rows*self.board.cols - 1} board challenge!\n"
        )
        print(
            f"You will see a board below with {self.board.rows*self.board.cols**2} squares containing numbers 1 to {self.board.rows*self.board.cols - 1} and an empty square, all randomly mixed."
        )
        print(
            "Your task is to slide adjacent squares into the empty square until you end up with the numbers in order, left to right, top to bottom with the empty square in the bottom right.\n"
        )
        print("Good luck!\n")
        print("#####################################\n")

    def play_game(self):
        """
        Allows user to input moves and checks updated board against the solution.
        When solution is reached, prints a congratulatory message and finishes game
        :return:
        """
        while not self.board.check_board_solved():
            self.board.present_board()
            move = self.parser.get_move_tuple_from_user()
            self.board.make_move(move)
        self._solution_message()

    def _solution_message(self):
        """
        Prints a congratulatory message
        :return:
        """
        print("\n\n****************** Well Done! ******************\n")
        self.board.present_board()
        print("\n************************************************")
