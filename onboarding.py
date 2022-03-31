import random


computer_wins = 0
player_wins = 0
games = 0
play = 'y'


while play == 'y':
    play = input('Do you want to play the game? Type y or n. ').lower()
    if play == 'y':
        games += 1
        print(games)
        player_choice = int(input('Write (0-paper, 1-rock, 2-scissors):  '))
        computer_choice = random.randint(0, 2)
        if player_choice == 0 and computer_choice == 1 or player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 0:
            player_wins += 1
            print('You chose', player_choice,  'Computer chose',
                  computer_choice, '. You won!')
        elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
            computer_wins += 1
            print('You chose', player_choice, 'Computer chose',
                  computer_choice, '. You lost!')
        elif player_choice == computer_choice:
            print('You chose the same. No winner in this round!')


print('Game is over. You won', player_wins, ', Computer won',
      computer_wins, ', times out of', games, '.')
