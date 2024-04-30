import random

def play_the_game():
    the_number_to_guess = random.randint(1, 100)
    guess = None
    the_number_of_guesses = 0
    player_name=str(input("What is the name that they call you in da hood? "))

    while guess != the_number_to_guess:
        guess = int(input("I'm thinking of a number between 1 - 100. What is it?"))
        the_number_of_guesses += 1

        if guess < the_number_to_guess:
            print("Too low to get unda'!")
        elif guess > the_number_to_guess:
            print("Too high to get ova'!")
        if guess == the_number_to_guess:    
            print(f"Alright, {player_name}! You did it! And it only took {the_number_of_guesses} tries to do it!")
        else:
            continue
if  __name__ == "__main__":
    play_the_game()
