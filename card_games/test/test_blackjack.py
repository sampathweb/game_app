#!/usr/bin/env python
"""
Test code for blackjack game.  Tests can be run with py.test or nosetests
"""
from __future__ import print_function
from unittest import TestCase
from card_games import blackjack
from card_games.blackjack import BlackJack

print(blackjack.__file__)


class TestRule(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        mygame = BlackJack()
        self.assertEqual(len(mygame.player_hand), 2)  # Initial hand for Player
        self.assertEqual(len(mygame.dealer_hand), 2)  # Initial hand for Dealer

    def test_player_bust(self):
        mygame = BlackJack()
        for cnt in range(10):  # Draw 10 cards - Sure to loose
            mygame.draw_card_player()
        self.assertEqual(len(mygame.player_hand), 12)  # Twelve cards in Player's hand
        self.assertEqual(mygame.game_result(), 'bust')  # Definitely a bust
