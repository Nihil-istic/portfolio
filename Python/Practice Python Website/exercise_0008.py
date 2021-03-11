'''
Exercise 8

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations 
to the winner, and ask if the players want to start 
a new game)
'''
def set_players():
    player_one = input('Name of player one: ')
    player_two = input('Name of player two: ')

    return player_one, player_two

def plays(player):
    print(f'Choose a play, {player}')
    print('0) rock')
    print('1) paper')
    print('2) scissors')

    while True:
        try:
            play = int(input('\n> '))

            if play in list(range(3)):
                pass
            else:
                raise ValueError

        except ValueError:
            print('You should type the number that corresponds to your play\n(0, 1, 2)\n')
            continue

        return play

def who_won(player_one, player_two, player_one_play, player_two_play):
    table = {
        '0': '1',
        '1': '2',
        '2': '0'
    }

    if player_one_play == player_two_play:
        return 'Draw!'
    
    elif table.get(player_one_play) == player_two_play:
        return f'{player_two} won!'
    
    elif table.get(player_two_play) == player_one_play:
        return f'{player_one} won!'
    
    else:
        return 'How the fuck did you ended here?'

def main():
    player_one, player_two = set_players()
    while True:

        player_one_play = plays(player_one)

        player_two_play = plays(player_two)

        print(who_won(player_one, player_two, str(player_one_play), str(player_two_play)))

        input('Press enter to play again ')

if __name__ == "__main__":
    main()
