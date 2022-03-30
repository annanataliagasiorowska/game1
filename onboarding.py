import random


computer_wins = 0
player_wins = 0
games = 0

while True:
    play = input('Do you want to play the game? Type yes or no. ').lower()
    if play == 'yes':
        games +=1
        print(games)
        player_choice = input('Write paper, rock, scissors: ').lower()
        choices = ['paper', 'rock', 'scissors']
        computer_choice = choices[random.randint(0,2)]
        if player_choice == 'paper' and computer_choice == 'rock' or player_choice == 'rock' and computer_choice == 'scissors' or player_choice == 'scissors' and computer_choice == 'paper':
            player_wins += 1 
            print('Computer chose', computer_choice,'. You won!')
        elif player_choice == 'paper' and computer_choice == 'scissors' or player_choice == 'rock' and computer_choice == 'paper' or player_choice == 'scissors' and computer_choice == 'rock':    
            computer_wins += 1    
            print('Computer chose', computer_choice,'. You lost!')
        elif player_choice == computer_choice:
            print('You chose the same. No winner in this round!')  
        

    else:
        break


print('Game is over. You won', player_wins, 'times out of', games,'.')


