import random 

# List of words used in the game
WORDS = ["python", "rich", "money", "lifestyle", "change", "job", "service", "helpful"]

def choose_the_word(word_list):
    """
    Choose a random word form the word list."""
    return random.choice(word_list)

def display_the_board(misses, correct_guesses, the_secret_word):
    """Shows what the game's lookin' like."""
    print("\nMisses: ", ' '.join(correct_guesses))
    the_displayed_word = [letter if letter in correct_guesses else '_' for letter in the_secret_word]
    print("Word: ", ''.join(the_displayed_word))

def get_the_guess():
    """Get the player's guess. Only accepts single characters."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Wrong answer, my guy! Please enter a single letter.")

def update_the_state_of_the_game(guess, the_secret_word, misses, correct_guesses):
    """Update exactly what the game is lookin' like based on the player's guess."""
    if guess in the_secret_word:
        correct_guesses.add(guess)
    else:
        misses.add(guess)

def play_hangman():
    the_secret_word = choose_the_word(WORDS)
    misses = set()
    correct_guesses = set()
    max_misses = 6

    while len (misses) < max_misses and not set (the_secret_word).issubset(correct_guesses):
        display_the_board(misses, correct_guesses, the_secret_word)
        guess = get_the_guess()
        update_the_state_of_the_game(guess, the_secret_word, misses, correct_guesses)
    
    if set(the_secret_word).issubset(correct_guesses):
        print("Congratulations, my guy! You guessed the correct word!", the_secret_word)
    else:
        print("Sorry, my guy! You ran out of chances. The word was...", the_secret_word)

if __name__ == "__main__":
    play_hangman()
