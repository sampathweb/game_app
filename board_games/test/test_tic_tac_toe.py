#!/usr/bin/env python

"""
test code for pychess rules module

can be run with py.test or nosetests
"""
from unittest import TestCase
from board_games import tic_tac_toe
from board_games.tic_tac_toe import TicTacToe

print(tic_tac_toe.__file__)


class TestRule(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        mytic = TicTacToe()
        self.assertEqual(mytic.game_result, None)

    def test_play_comp_level_1(self):
        mytic = TicTacToe(play_computer=True, level=1)
        mytic.player_a_move(0, 0)
        if (0, 1) in mytic.open_positions:
            mytic.player_a_move(0, 1)
        else:
            mytic.player_a_move(1, 1)
        self.assertEqual(len(mytic.player_b_choices), 2)  # Three moves by Computer

    def test_play_comp_level_2(self):
        mytic = TicTacToe(play_computer=True, level=2)
        mytic.player_a_move(1, 0)
        if (1, 1) in mytic.open_positions:
            mytic.player_a_move(1, 1)
        else:
            mytic.player_a_move(2, 1)
        self.assertEqual(len(mytic.player_b_choices), 2)  # Three moves by Computer

    def test_player_a_win_row(self):
        mytic = TicTacToe()
        mytic.player_a_move(0, 0)
        mytic.player_a_move(0, 1)
        mytic.player_a_move(0, 2)
        self.assertEqual(mytic.game_result, 'A')

    def test_player_a_win_col(self):
        mytic = TicTacToe()
        mytic.player_a_move(2, 0)
        mytic.player_a_move(2, 1)
        mytic.player_a_move(2, 2)
        self.assertEqual(mytic.game_result, 'A')

    def test_player_a_win_diag(self):
        mytic = TicTacToe()
        mytic.player_a_move(0, 0)
        mytic.player_a_move(1, 1)
        mytic.player_a_move(2, 2)
        self.assertEqual(mytic.game_result, 'A')

    def test_player_b_win_row(self):
        mytic = TicTacToe()
        mytic.player_b_move(1, 0)
        mytic.player_b_move(1, 1)
        mytic.player_b_move(1, 2)
        self.assertEqual(mytic.game_result, 'B')

    def test_player_b_win_col(self):
        mytic = TicTacToe()
        mytic.player_b_move(1, 0)
        mytic.player_b_move(1, 1)
        mytic.player_b_move(1, 2)
        self.assertEqual(mytic.game_result, 'B')

    def test_player_b_win_diag(self):
        mytic = TicTacToe()
        mytic.player_b_move(0, 2)
        mytic.player_b_move(2, 0)
        mytic.player_b_move(1, 1)
        self.assertEqual(mytic.game_result, 'B')

    def test_draw(self):
        mytic = TicTacToe()
        mytic.player_a_move(1, 0)
        mytic.player_a_move(1, 1)
        mytic.player_b_move(1, 2)
        # mytic.player_a_move(0, 0)
        mytic.player_b_move(0, 1)
        mytic.player_a_move(0, 2)
        mytic.player_b_move(2, 0)
        mytic.player_a_move(2, 1)
        mytic.player_b_move(2, 2)
        self.assertEqual(mytic.game_result, 'D')

    def test_all_moves_draw(self):
        mytic = TicTacToe()
        mytic.player_a_move(1, 0)
        mytic.player_a_move(1, 1)
        mytic.player_b_move(1, 2)
        mytic.player_a_move(0, 0)
        mytic.player_b_move(0, 1)
        mytic.player_a_move(0, 2)
        mytic.player_b_move(2, 0)
        mytic.player_a_move(2, 1)
        mytic.player_b_move(2, 2)
        self.assertEqual(mytic.game_result, 'D')

    def test_game_not_over(self):
        mytic = TicTacToe()
        mytic.player_a_move(1, 0)
        mytic.player_a_move(1, 1)
        mytic.player_b_move(1, 2)
        self.assertEqual(mytic.game_result, None)
