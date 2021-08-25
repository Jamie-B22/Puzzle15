"""
    Author: Jamie Bamforth
    Tests code in board_cls.py and the create_game() function in main
"""

import unittest
from main import create_game
from board_cls import SquarePuzzleBoard
from input_parser_cls import InputParser
from game_cls import PuzzleGame


class TestInputParser(unittest.TestCase):
    def test_init(self):
        game = create_game()
        self.assertTrue(isinstance(game, PuzzleGame))
        self.assertTrue(isinstance(game.board, SquarePuzzleBoard))
        self.assertTrue(isinstance(game.parser, InputParser))


if __name__ == "__main__":
    unittest.main()
