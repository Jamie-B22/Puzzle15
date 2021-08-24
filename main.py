"""
    Author: Jamie Bamforth
    main script for running Puzzle15 game.
"""
from config import SQUARE_BOARD_SIDE_LENGTH
from board_cls import SquarePuzzleBoard
from input_parser_cls import InputParser



# TODO: move all into some sort of game class
# TODO: write a load of tests for the game class, how do you mock up system input?
if __name__ == '__main__':
    board = SquarePuzzleBoard(SQUARE_BOARD_SIDE_LENGTH)
    rows, cols = board.board_side_length, board.board_side_length
    parser = InputParser(rows, cols)

    print('Welcome to the Puzzle15 board challenge!\n')
    print(f'You will see a board below with {rows * cols} squares containing numbers 1 to {rows * cols - 1} and an empty square, all randomly mixed.')
    print('Your task is to slide adjacent squares into the empty square until you end up with the numbers in order, left to right, top to bottom with the empty square in the bottom right.\n')
    print('Good luck!\n')
    print('#####################################\n')
    while not board.check_board_solved():
        board.present_board()
        move = parser.get_move_tuple_from_user()
        board.make_move(move)
    print('\n\n************ Well Done! ******************')


