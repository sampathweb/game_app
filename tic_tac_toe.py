#! /usr/bin/env python
from random import choice
from collections import defaultdict

def get_player_input(valid_selections):
    '''Returns the selected row, col by the Player'''
    selected_item = tuple()
    while selected_item not in valid_selections:
        if selected_item:
            print('Your selection of (%s, %s) is not valid: ' % selected_item)
        selected_item = tuple(int(val) for val in input('Enter your selection in row, col format:').split(',') if val.isdigit())
    return selected_item

def get_computer_input(valid_choices, winning_combos, player_choices, current_choices, dif_level):
    '''Returns the computer selected row, col'''
    choices = defaultdict(list)
    choices = defaultdict(list)
    if dif_level == 1:  # Easy - Pick any one from valid_choices list
        selected_item = choice(valid_choices)
    elif dif_level == 2:  # Hard - Try to block the player from winning
        for win_set in winning_combos:
            rem_items = list(win_set - player_choices - current_choices)
            choices[len(rem_items)].append(rem_items)
        if choices.get(1):
            selected_item = choices[1][0][0]
        elif choices.get(2):
            selected_item = choices[2][0][0]
        else:
            selected_item = choices[3][0][0]
    else:   # Ultimate
        for win_set in winning_combos:
            rem_items = list(win_set - current_choices)
            choices_ult[len(rem_items)].append(rem_items)
            rem_items = list(win_set - player_choices)
            choices[len(rem_items)].append(rem_items)
            
        if choices_ult.get(1):
            selected_item = choices_ult[1][0][0]
        if choices.get(1):
            selected_item = choices[1][0][0]
        if choices_ult.get(2):
            selected_item = choices_ult[1][0][0]            
        elif choices.get(2):
            selected_item = choices[2][0][0]
        else:
            selected_item = choices[3][0][0]
        pass
    return selected_item

def print_positions(player_a, playera_choices, player_b, playerb_choices):
    '''Returns None.  Prints the current Positions'''
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for row in range(3):
        print(row, end=' |')
        for col in range(3):
            if (row, col) in playera_choices:
                print('', player_a, end=' |')
            elif (row, col) in playerb_choices:
                print('', player_b, end=' |')
            else:
                print('   ', end='|')
        print('')

def check_winning_combinations(player_choices, winning_combos):
    '''Returns True if Player has a winning combination'''
    for win_set in winning_combos:
        if win_set.issubset(player_choices):
            return True
    return False

def play_tic_tac_toe(player_a='X', player_b='O', dif_level=1):
    '''Plays the game of Tic-Tac-Toe.  If player_b is None, Player A Plays with the Computer at dif level'''
    #Initialize the count on row, col and diag axis for Player and Computer
    game_choices = []
    for row in range(3):
        for col in range(3):
            game_choices.append((row,col))
    winning_combos = []
    for row in range(3):
        win_set = set()
        for col in range(3):
            win_set.add((row,col))
        winning_combos.append(win_set)    
    for col in range(3):
        win_set = set()
        for row in range(3):
            win_set.add((row,col))
        winning_combos.append(win_set)
    winning_combos.append(set([(0,0), (1,1), (2,2)]))
    winning_combos.append(set([(0,2), (1,1), (2,0)]))
    player_a_choices = set()
    player_b_choices = set()
    print('Game Choices: %s' %game_choices)
    print('Good Luck!', end='\n\n')
    player_a_turn = True
    while game_choices and winning_combos:
        # Print the current positions - only print when it's player A's turn or a two player game
        if player_a_turn or player_b:
            print_positions(player_a, player_a_choices, player_b, player_b_choices)
        if player_a_turn:
            selected_item = get_player_input(game_choices)
            player_a_choices.add(selected_item)
            if check_winning_combinations(player_a_choices, winning_combos):
                result = 'A'
                break
        else:
            selected_item = get_computer_input(game_choices, winning_combos, player_a_choices, player_b_choices, dif_level)          
            player_b_choices.add(selected_item)
            if check_winning_combinations(player_b_choices, winning_combos):
                result = 'B'
                break
        game_choices.remove(selected_item)
        # Reduce the winning combo list if both player A and B have items in that set
        for win_set in winning_combos:
            rem_set_a = win_set - player_a_choices
            rem_set_b = win_set - player_b_choices
            if len(rem_set_a) < 3 and len(rem_set_b) < 3:
                winning_combos.remove(win_set)
        player_a_turn = not player_a_turn  #On next loop, it's the other player's turn
    # Print the final Positions before quiting the game
    if not winning_combos:
        result = 'D'
    print_positions(player_a, player_a_choices, player_b, player_b_choices)
    return result

if __name__ == '__main__':
    print('Welcome to a game of Tic-Tac-Toe')
    player_a = input('Enter your Name: ').strip()
    if not player_a:
        player_a = 'You'
    while True:
        dif_level = input('Select difficult level (1 - Easy, 2 - Hard, 3 - Ultimate): ')
        if dif_level.isdigit():
            dif_level = int(dif_level)
        else:
            dif_level = 1
        result = play_tic_tac_toe('X', 'O', dif_level=dif_level)
        if result == 'A':
            print('%s Won.  Congratulations!' % player_a)
        elif result == 'B':
            print('Computer Wins.  Better luck next time!')
        elif result == 'D':
            print('Its a Draw.')
        if input('Do you want to play again Y/N: ').strip().upper() == 'N':
            break

