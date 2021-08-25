"""
    Author: Jamie Bamforth
    Class to take and check input from the user.
"""


class InputParser:
    def __init__(self, n_board_rows, n_board_cols):
        self._n_board_rows = n_board_rows
        self._n_board_cols = n_board_cols

    def get_move_tuple_from_user(self) -> tuple:
        row = self._get_valid_row_input()
        col = self._get_valid_col_input()
        return row, col

    def _get_valid_row_input(self) -> int:
        # TODO: check if alpha value
        ask_for_input = True
        while ask_for_input:
            row = int(
                input(
                    f"Please enter the row of the square you would like to move. Rows are from 0 to {self._n_board_rows-1}, starting with 0 as the top row.\nRow: "
                )
            )

            if row < self._n_board_rows and row >= 0:
                ask_for_input = False
            else:
                print("Please enter a valid row.")
        return row

    def _get_valid_col_input(self) -> int:
        ask_for_input = True
        while ask_for_input:
            col = int(
                input(
                    f"Please enter the column of the square you would like to move. Columns are from 0 to {self._n_board_cols-1}, starting with 0 as the top column.\nColumn: "
                )
            )

            if col < self._n_board_rows and col >= 0:
                ask_for_input = False
            else:
                print("Please enter a valid column.")
        return col
