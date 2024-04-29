import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    guess = -1

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guess != number_to_guess:
        number_of_guesses += 1
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("You went ova'! Pick a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {number_of_guesses} tries!")
                break
        except ValueError:
            print("That's not a good answer, my guy. Please put in a number between 1 and 100.")

# Run the game
guess_number()
