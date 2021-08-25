"""
    Author: Jamie Bamforth
    Class for creating a game.
"""


class PuzzleGame:
    def __init__(self, board, parser):
        self.board = board
        self.parser = parser

    def intro_message(self):
        print("Welcome to the Puzzle15 board challenge!\n")
        print(
            f"You will see a board below with {self.board.board_side_length**2} squares containing numbers 1 to {self.board.board_side_length**2 - 1} and an empty square, all randomly mixed."
        )
        print(
            "Your task is to slide adjacent squares into the empty square until you end up with the numbers in order, left to right, top to bottom with the empty square in the bottom right.\n"
        )
        print("Good luck!\n")
        print("#####################################\n")

    def play_game(self):
        while not self.board.check_board_solved():
            self.board.present_board()
            move = self.parser.get_move_tuple_from_user()
            self.board.make_move(move)
        self._solution_message()

    def _solution_message(self):
        print("\n\n****************** Well Done! ******************\n")
        self.board.present_board()
        print("\n************************************************")
