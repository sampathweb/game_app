#!/usr/bin/env python
"""
A package to wrap the rules of BlackJack.
"""
from __future__ import print_function
import random


class BlackJack:

    def __init__(self, play_computer=True, level=0):
        self.play_computer = play_computer
        self.level = level
        self.card_suits = ['spade', 'heart', 'diamond', 'club']
        self.card_faces = {str(numb): numb for numb in range(2, 11)}
        for face in ('jack', 'king', 'queen'):
            self.card_faces[face] = 10
        self.card_faces['ace'] = 1
        self._reset_board()

    def _face_value(self, face_numb):
        '''Returns card value for the card. Card needs to be of format (face, suit)'''
        return self.card_faces[face_numb]

    def get_hand_value(self, hand):
        hand_values = [0]
        for face, suit in hand:
            card_value = self._face_value(face)
            hand_values = [value + card_value for value in hand_values]
            if face == 'ace':
                hand_values_ace = [value + 10 for value in hand_values if value <= 11]
                hand_values += hand_values_ace
        # Exclude all values > 21
        hand_values.sort(reverse=True)  # Highest number First
        for value in hand_values:
            hand_value = value
            if hand_value <= 21:  # Found the highest number <= 21
                break
        return hand_value

    def _reset_board(self):
        '''Initiailizes the available cards and the hands of Player and Dealer'''
        self.player_hand = []
        self.dealer_hand = []
        self.card_deck = [(face, suit) for suit in self.card_suits for face in self.card_faces.keys()]
        random.shuffle(self.card_deck)  # Shuffle the card deck
        # Draw two cards for Player and Dealer
        self.player_hand.append(self._pick_card())
        self.player_hand.append(self._pick_card())
        self.dealer_hand.append(self._pick_card())
        self.dealer_hand.append(self._pick_card())

    def _pick_card(self):
        '''Draws a Card from the Deck and return the card'''
        return self.card_deck.pop()

    def draw_card_player(self):
        self.player_hand.append(self._pick_card())

    def player_hand_value(self):
        return self.get_hand_value(self.player_hand)

    def dealer_hand_value(self):
        return self.get_hand_value(self.dealer_hand)

    def game_result(self):
        dealer_value = self.dealer_hand_value()
        player_value = self.player_hand_value()
        if player_value > 21:
            result = 'bust'
        elif dealer_value > 21:
            result = 'won'
        elif player_value > dealer_value:
            result = 'won'
        elif dealer_value > player_value:
            result = 'lost'
        elif player_value == dealer_value:
            result = 'push'
        else:
            result = None
        return result
