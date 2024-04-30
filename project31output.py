import random 

def get_the_player_name():
    """Asks the user for their name"""
player_name = input("What's your name that they call you in da hood?")

def get_the_computer_choice():
    """Returns a random choice between 'rock' , 'paper', 'scissors', 'stick', 'knife' 'gun' and 'cell phone'"""
    choices = ['rock','paper','scissors']
    return random.choice(choices)

def get_the_winner(player_choice, computer_choice):
    """Declares who won the game."""
    
    if (player_choice =='rock' and computer_choice =='scissors') or \
         (player_choice =='scissors' and computer_choice == 'paper') or \
         (player_choice =='paper' and computer_choice == 'rock') or \
         (player_choice == 'stick' and computer_choice == 'rock') or \
         (player_choice == 'stick' and computer_choice == 'paper') or \
         (player_choice == 'stick' and computer_choice == 'scissors') or \
         (player_choice == 'knife' and computer_choice == 'stick') or \
         (player_choice == 'knife' and computer_choice == 'rock') or \
         (player_choice == 'knife' and computer_choice == 'paper') or \
         (player_choice == 'knife' and computer_choice == 'scissors') or \
         (player_choice == 'gun' and computer_choice == 'rock') or \
         (player_choice == 'gun' and computer_choice == 'scissors') or \
         (player_choice == 'gun' and computer_choice == 'paper') or \
         (player_choice == 'gun' and computer_choice == 'knife') or \
         (player_choice == 'gun' and computer_choice == 'stick') or \
         (player_choice == 'cell phone' and computer_choice == 'rock') or \
         (player_choice == 'cell phone' and computer_choice == 'scissors') or \
         (player_choice == 'cell phone' and computer_choice == 'paper') or \
         (player_choice == 'cell phone' and  computer_choice == 'gun') or \
        (player_choice == 'cell phone' and computer_choice == 'stick') or \
        (player_choice == 'cell phone' and computer_choice == 'knife'):
        return 'player'
    else:
        return 'computer'

def weapon_unlocked(player_choice, computer_choice):
    player_score = 0
    computer_score = 0
    choices = ['rock','paper','scissors']

    if player_choice > computer_choice:
        player_score +=1
    elif player_choice < computer_choice:
        computer_score +=1
    if player_score==4:
        print("{player_name} has unlocked the stick! Type 'stick' to use it!")
        choices.append("stick")
    elif computer_score ==4:
        print("The computer has unlocked the stick!")
        choices.append("stick")
    if player_score ==6:
        print("{player_name} has unlocked the knife! Type 'knife' to use it.")
        choices.append("knife")
    elif computer_score ==6:
        print("The computer has unlocked the knife!")
        choices.append("knife")
    if player_score ==8:
        print("{player_name} has unlocked the gun!  Type 'gun' to use it.")
        choices.append("gun")
    elif computer_score ==8:
        print("The computer has unlocked the gun!")
        choices.append("gun")
    if player_score ==10: 
        print("{player_name} has unlocked the cell phone!  Type 'cell phone' to use it.")
        choices.append("cell phone")
    elif computer_score ==10:
        print("The computer has unlocked the cell phone!")
        choices.append("cell phone")
    if player_score != 4 and input == 'stick':
        return "Put that stick down! You haven't earned the right to use it!"
    if player_score != 6 and input == 'knife':
        return "Put that knife down! You can't cut up just yet!"
    if player_score != 8 and input ==  'gun':
        return "Put that gun down! You ain't got no license for that."
    if player_score != 10 and input == 'cell phone':
        return "Put that phone down! Ain't nobody callin' you!"
    if player_choice < computer_choice:
        player_score -=1
    else:
        computer_score -=1
    if player_choice < computer_choice and player_score == 4:
        player_score -=1 and choices.remove('stick')
    elif computer_choice < player_choice and computer_score == 4:
        computer_score -=1 and choices.remove('stick')
    if player_choice < computer_choice and player_score == 6:
        player_score -=1 and choices.remove('knife')
    elif  computer_choice > player_choice and computer_score == 6:
        computer_score -=1 and choices.remove('knife')
    if player_choice < computer_choice and player_score == 8:
        player_score -=1 and choices.remove('gun')
    elif computer_choice < player_choice and computer_score == 8:
        computer_score -=1 and choices.remove('gun')
    if player_choice <  computer_choice and player_score == 10:
        player_score -=1 and choices.remove('cell phone')
    elif  computer_choice > player_choice and computer_score == 10:
        computer_score -=1 and choices.remove('cell phone')
 
def main():
    """The main function of this game."""
    print("Let's play Rock, Paper, Scissors, Version 2!")
    while True:
        player_choice=input("Enter your choice (rock, paper, scissors) or 'quit' to exit:  ").lower()
        if  player_choice=='quit':
            break
        computer_choice=get_the_computer_choice()
        print("The computer chose: ", computer_choice)
        new_weapon = weapon_unlocked(player_choice, computer_choice)
        winner = get_the_winner(player_choice, computer_choice)
        if player_choice == computer_choice:
            return 'tie'
        elif winner == 'player':
            print("You win!")
        else:
            print("The computer wins!")

if  __name__=="__main__":
    main()
