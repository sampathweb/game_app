        if self.level == 0:  # Easy - Pick any one from valid_choices list
        selected_item = choice(self.open_positions)
        elif self.level == 1:  # Hard - Try to block the player from winning
            for win_set in self.winning_combos:
                rem_items = list(win_set - self.player_choices - self.current_choices)
                selections[len(rem_items)].append(rem_items)
            if selections.get(1):
                selected_item = choice(choice(selections[1]))
            elif selections.get(2):
                selected_item = choice(choice(selections[2]))
            else:
                selected_item = choice(choice(selections[3]))



    def play_tic_tac_toe(player_a='X', player_b='O'):
        '''Plays the game of Tic-Tac-Toe.  If player_b is None, Player A Plays with the Computer at dif level'''
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
        dif_level = input('Select difficult level (1 - Easy, 2 - Hard): ')
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
