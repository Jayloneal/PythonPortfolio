import random 

# Function to get the computer's choice
def  get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to get the user's choice
def  get_user_choice():
    choice = input("Enter Rock, Paper or Scissors, my guy: ").capitalize()
    while choice not in ["Rock", "Paper", "Scissors"]:
        print("Bad choice, my guy! Please pick either Rock, Paper or Scissors.")
        choice = input("Enter Rock, Paper or Scissors: ").capitalize()
    return choice

# Function to determine who wins.
def determine_who_wins(user_choice, computer_choice):
    if user_choice == computer_choice:
         return "That's a draw!"
    elif (user_choice=="Rock" and computer_choice=="Scissors") or \
    (user_choice=="Scissors" and computer_choice=="Paper") or \
    (user_choice=="Paper" and computer_choice=="Rock"):
        return f"You won, my guy! It's ova' and done wit'!"
    else:
        return "You lost, bruh! It's ova' and done wit'!"
    
# Main gameplay
def play_the_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")
    result = determine_who_wins(user_choice, computer_choice)
    print(result)

# Play the game
if __name__ == "__main__":
    play_again = 'y'
    while play_again.lower() =='y':
        play_the_game()
        play_again = input("Wanna play again, my guy? (Y/N): ")

print("Appreciate y'all for playin'!")
