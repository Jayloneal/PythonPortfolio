import random

def roll_die():
    """Roll the die and get a number between 1 and 6."""
    return random.randint(1,6)

def turn(player_name):
    player_name = "Jaylon"
    """Act as if it's someone's turn and return the score for that turn."""
    turn_score = 0
    rolling = True 
    while rolling:
        roll = roll_die()
        print(f"{player_name} rolled a {roll}.")

        if roll ==1:
            print(f"Sorry {player_name}! You rolled a 1. No points for you, my guy!")
            return 0
        else:
            turn_score += roll
            print(f"{player_name}'s total is {turn_score}")

            if player_name != 'Computer':
                response = input("Roll again, my guy? (y/n): ").lower()
                rolling = response == 'y'
            else: 
                rolling = turn_score < 20 # Simple strategy for the computer: stop rolling if turn score is 20 or higher
    return turn_score

def main():
    player_score = 0
    computer_score = 0

    while player_score < 100 and computer_score < 100:
        print("\nYour turn!")
        player_score += turn("Player")
        print(f"Your total score is {player_score}\n")

        if player_score >=  100:
            break

        print("Computer's turn!")
        computer_score += turn("Computer")
        print(f"Computer's total score is {computer_score}\n")

        if player_score >= 100:
            print("Congratulations, my guy! You won!")
        else:
            print("Computer wins! Keep trying, my guy! You'll get 'im next time!")

if __name__== "__main__":
    print("Welcome to the game of Pig!")
    main()
            
