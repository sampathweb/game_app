#!/usr/bin/env python
"""
A package to wrap the rules of PawnChess.
"""


class PawnChess:

    def __init__(self, play_computer=False, level=0):
        self.play_computer = play_computer
        self.level = level
        self._reset_board()

    def _reset_board(self):
        #Initialize the count on row, col and diag axis for Player and Computer
        self.open_positions = []
        self.game_result = None
        # Build a 3X3 List of tuples for each cell
        for row in range(8):
            for col in range(8):
                self.open_positions.append((row, col))
        # Reset the Pieces on the board
        self.player_a_choices = set()
        self.player_b_choices = set()
