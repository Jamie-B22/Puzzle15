"""
    Author: Jamie Bamforth
    main script for running Puzzle15 game.
"""
from config import SQUARE_BOARD_SIDE_LENGTH
from board_cls import PuzzleBoard
from input_parser_cls import InputParser
from game_cls import PuzzleGame

def create_game() -> PuzzleGame:
    board = PuzzleBoard(SQUARE_BOARD_SIDE_LENGTH, SQUARE_BOARD_SIDE_LENGTH)
    rows, cols = board.rows, board.cols
    parser = InputParser(rows, cols)
    return PuzzleGame(board, parser)


if __name__ == "__main__":
    game = create_game()
    game.intro_message()
    game.play_game()
