"""
    Author: Jamie Bamforth
    Class to take and check input from the user.
"""


class InputParser:
    def __init__(self, n_board_rows: int, n_board_cols: int):
        self._n_board_rows = n_board_rows
        self._n_board_cols = n_board_cols

    def get_move_tuple_from_user(self) -> tuple:
        """
        Get the input from the user and return a move tuple
        :return: move tuple format (row, column)
        """
        row = self._get_valid_int_input("row", self._n_board_rows)
        col = self._get_valid_int_input("column", self._n_board_cols)
        return row, col

    def _get_valid_int_input(self, type: str, dimension_size: int) -> int:
        """
        Takes a type string to inform the user in the input message and returns a valid integer from user input
        :param type: string of value 'row' or 'column'
        :param dimension_size: number of possible integers to give an upper limit
        :return: integer of input given
        """
        ask_for_input = True
        while ask_for_input:
            num, valid = self._get_and_validate_int_input(type, dimension_size)
            ask_for_input = not valid
        return int(num)

    @staticmethod
    def _get_and_validate_int_input(type: str, dimension_size: int) -> tuple:
        """
        Splits out the validation step and from the while loop for testing reasons
        :param type: string of value 'row' or 'column'
        :param dimension_size: number of possible integers to give an upper limit
        :return: tuple of user input and validation bool
        """
        valid = False
        num = input(
            f"Please enter the {type} of the square you would like to move. {type.title()}s are from 0 to {dimension_size - 1}, starting from top left.\n{type}: "
        )
        if not num.isnumeric():
            # check first and separately to prevent an exception being thrown on int() type conversion
            print(f"Please enter a valid {type}.")
        elif int(num) >= dimension_size or int(num) < 0:
            print(f"Please enter a valid {type}.")
        else:
            valid = True
        return num, valid
