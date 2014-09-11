#!/usr/bin/env python
from __future__ import print_function
from blackjack import BlackJack


def play_blackjack(player):
    game = BlackJack()
    while True:
        print('Your Hand %s is of value %d' % (game.player_hand, game.player_hand_value()))
        action = raw_input('Enter: hit (1), stand (2) or split (3) or help (h): ').upper()
        if action == '2':  # Stand
            result = game.game_result()
            print('Dealer Hand %s is of value %d' % (game.dealer_hand, game.dealer_hand_value()))
            print('Result is: ', result)
            print('Round Over.')
            return result
        elif action == '1':  # Hit
            game.draw_card_player()
        elif action == 'H':  # Help
            print('Your Hand Score is: ', game.player_hand_value())
            print('You can Hit (1): Draw one more card to see if you get closer to 21, but not higher.')
            print('You can Stand (2): Compare your current hand value with Dealer hand value to see if you scored higher, but still 21 or below.')
            print('You can Split (3): ')
            print('You can double down (4): ')

if __name__ == '__main__':
    player = {}
    player['chips'] = 100
    player['round'] = 0
    player['won'] = 0
    player['lost'] = 0
    player['push'] = 0
    player['bust'] = 0
    play = 'Y'
    print('Welcome to BlackJack')
    print('-' * 20)
    print('You have 100 Chips to play this game.  On each round, you will have to pitch atleast one chip.  You can wager more.')
    while play != 'N':
        play = raw_input('Play a round of BlackJack (Y/N)? ').upper()
        chips = raw_input('How many chips do you wager? (min 1, max %d): ' % player['chips'])
        if play.upper() == 'Y':
            player['round'] += 1
            result = play_blackjack(player)
            player[result] += 1
