import random

def play_game():
    print("Let's play the number guessing game, version 2!")
    print("")
    level = input("Select the difficulty level (easy, medium, hard): ").lower()
    guess_range = 0
    guesses_allowed = 0
    if level == "easy":
        guess_range = 50
        guesses_allowed = 30
    elif level == "medium":
        guess_range = 100
        guesses_allowed = 13
    else:
        guess_range = 200
        guesses_allowed = 10

    answer = random.randint(1, guess_range)
    guess = ""
    attempts = 0
    while guess != answer:
        userInput = input("You have to guess a number between 1 and " + str(guess_range) + ": ")
        guess = int(userInput)
        attempts += 1
        if guess == answer:
            print("Good job, my guy! You guessed the right number!")
            break
        elif guess < answer:
            print("Too high to get ova'!")
            if abs(guess - answer) <= 10:
                print("My boy, you close!")
            elif abs(guess - answer) <= 20:
                print("You almost there.")
            else:
                print("You not even close.")
        else:
            print("Too low to get unda'!")
            if abs(guess - answer) <= 10:
                print("My boy, you close!")
            elif abs(guess - answer) <= 20:
                print("You almost there.")
            else:
                print("You not even close.")
        if attempts == guesses_allowed:
            print("Sorry, my guy! You ran outta guesses!")
            break

    play_again = input("Wannna play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()

play_game()
