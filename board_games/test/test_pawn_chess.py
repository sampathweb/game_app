#!/usr/bin/env python

"""
test code for pychess rules module

can be run with py.test or nosetests
"""
from unittest import TestCase

from board_games import pawn_chess
from board_games.pawn_chess import PawnChess

print(pawn_chess.__file__)


class TestRule(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
