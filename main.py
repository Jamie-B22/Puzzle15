"""
    Author: Jamie Bamforth
    main script for running Puzzle15 game.
"""
from config import SQUARE_BOARD_SIDE_LENGTH
from board_cls import SquarePuzzleBoard
from input_parser_cls import InputParser
from game_cls import PuzzleGame

def create_game() -> PuzzleGame:
    board = SquarePuzzleBoard(SQUARE_BOARD_SIDE_LENGTH)
    rows, cols = board.board_side_length, board.board_side_length
    parser = InputParser(rows, cols)
    return PuzzleGame(board, parser)


if __name__ == "__main__":
    game = create_game()
    game.intro_message()
    game.play_game()
