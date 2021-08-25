"""
    Author: Jamie Bamforth
    Tests code in board_cls.py and the create_game() function in main
"""

import unittest
import builtins
from input_parser_cls import InputParser
from contextlib import contextmanager


@contextmanager  # mocks up user input in context
def mockRawInput(mock):
    original_raw_input = builtins.input
    builtins.input = lambda _: mock
    yield
    builtins.input = original_raw_input


class TestInputParser(unittest.TestCase):
    def test_init(self):
        parser = InputParser(3,4)
        self.assertEqual(parser._n_board_rows, 3)
        self.assertEqual(parser._n_board_cols, 4)

    def test_valid_input(self):
        with mockRawInput("1"):
            result = InputParser._get_and_validate_int_input("row", 4)
            self.assertEqual(result, ("1", True))

        with mockRawInput("0"):
            result = InputParser._get_and_validate_int_input("test", 100)
            self.assertEqual(result, ("0", True))

        with mockRawInput("99"):
            result = InputParser._get_and_validate_int_input("test", 100)
            self.assertEqual(result, ("99", True))

        with mockRawInput("3"):
            result = InputParser._get_and_validate_int_input("row", 10)
            self.assertEqual(result, ("3", True))

    def test_invalid_input(self):
        with mockRawInput("-1"):
            result = InputParser._get_and_validate_int_input("row", 4)
            self.assertEqual(result, ("-1", False))

        with mockRawInput("1000"):
            result = InputParser._get_and_validate_int_input("test", 100)
            self.assertEqual(result, ("1000", False))

        with mockRawInput("100"):
            result = InputParser._get_and_validate_int_input("test", 100)
            self.assertEqual(result, ("100", False))

        with mockRawInput("99"):
            result = InputParser._get_and_validate_int_input("row", 10)
            self.assertEqual(result, ("99", False))


if __name__ == "__main__":
    unittest.main()
