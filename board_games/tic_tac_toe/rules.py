#!/usr/bin/env python
"""
A package to wrap the rules of TicTacToe.
"""
from __future__ import print_function
from random import choice
from collections import defaultdict


class TicTacToe:

    def __init__(self, play_computer=False, level=0):
        self.play_computer = play_computer
        self.level = level
        self._reset_board()

    def _reset_board(self):
        #Initialize the count on row, col and diag axis for Player and Computer
        self.open_positions = []
        self.winning_combos = []
        self.game_result = None
        # Build a 3X3 List of tuples for each cell
        for row in range(3):
            for col in range(3):
                self.open_positions.append((row, col))
        # Define the winning combinations by row
        for row in range(3):
            win_set = set()
            for col in range(3):
                win_set.add((row, col))
            self.winning_combos.append(win_set)
        # Define the winning combinations by Col
        for col in range(3):
            win_set = set()
            for row in range(3):
                win_set.add((row, col))
            self.winning_combos.append(win_set)
        # Define the winning combinations by Diagonal
        self.winning_combos.append(set([(0, 0), (1, 1), (2, 2)]))
        self.winning_combos.append(set([(0, 2), (1, 1), (2, 0)]))
        # Reset the Pieces on the board
        self.player_a_choices = set()
        self.player_b_choices = set()

    def is_open_position(self, selected_item):
        '''Returns the selected row, col by the Player'''
        if selected_item in self.open_positions:
            return True
        return False

    def setup_board(self, player_a, player_b):
        '''Sets up board for Player A and B'''
        move_combos = zip(player_a, player_b)
        for combo in move_combos:
            self.player_a_choices.add(combo[0])
            self._remove_open_position(combo[0])
            self.player_b_choices.add(combo[1])
            self._remove_open_position(combo[1])
        # Last move of Player A needs to be handled in addition
        row, col = player_a[-1]
        self.player_a_move(row, col, auto_play=False)

    def player_a_move(self, row, col, auto_play=True):
        '''Returns the selected row, col by the Player'''
        selected_item = (row, col)
        if self.is_open_position(selected_item):
            self.player_a_choices.add(selected_item)
            self._remove_open_position(selected_item)
            self._compute_game_result()
            if not self.game_result and self.play_computer and auto_play:
                self.player_b_move()

    def player_b_move(self, row=None, col=None):
        '''Returns the selected row, col by the Player'''
        if self.play_computer:
            selected_item = self._pick_computer_move()
            self.player_b_choices.add(selected_item)
        else:
            selected_item = (row, col)
            if self.is_open_position(selected_item):
                self.player_b_choices.add(selected_item)
        self._remove_open_position(selected_item)
        self._compute_game_result()
        return selected_item

    def _pick_computer_move(self):
        '''Returns the computer selected row, col'''
        selections = defaultdict(list)
        if self.level == 1:  # Easy - Pick any one from valid_choices list
            selected_item = choice(self.open_positions)
        elif self.level == 2:  # Hard - Try to block the player from winning
            for win_set in self.winning_combos:
                rem_items = list(win_set - self.player_a_choices - self.player_b_choices)
                selections[len(rem_items)].append(rem_items)
            if selections.get(1):
                selected_item = choice(choice(selections[1]))
            elif selections.get(2):
                selected_item = choice(choice(selections[2]))
            else:
                selected_item = choice(choice(selections[3]))
        return selected_item

    def _remove_open_position(self, selected_item):
        if selected_item in self.open_positions:
            self.open_positions.remove(selected_item)
        # Reduce the winning combo list if both player A and B have items in that set
        for win_set in self.winning_combos:
            rem_set_a = win_set - self.player_a_choices
            rem_set_b = win_set - self.player_b_choices
            if len(rem_set_a) < 3 and len(rem_set_b) < 3:
                self.winning_combos.remove(win_set)

    def print_positions(self, player_a='X', player_b='O'):
        '''Returns None.  Prints the current Positions'''
        print('  | 0 | 1 | 2 |')
        print('---------------')
        for row in range(3):
            print(row, end=' |')
            for col in range(3):
                if (row, col) in self.player_a_choices:
                    print('', player_a, end=' |')
                elif (row, col) in self.player_b_choices:
                    print('', player_b, end=' |')
                else:
                    print(' _ ', end='|')
            print('')

    def _compute_game_result(self):
        '''Returns True if Game has ended with a Winner or Draw, else returns False'''
        if self.game_result:
            return True
        if not self.winning_combos:
            self.game_result = 'D'
            return True
        for win_set in self.winning_combos:
            if win_set.issubset(self.player_a_choices):
                self.game_result = 'A'
                return True
            if win_set.issubset(self.player_b_choices):
                self.game_result = 'B'
                return True
        return False  # Keep Playing, the play has not ended
