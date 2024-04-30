import random 

def choose_the_word():
    words = ["bowling", "fishing", "hiking", "biking", "kite flying", "fighting", "boxing", "shooting", "swinging", "swimming", "dancing", "driving", "running", "exercising", "singing", "playing"]
    return random.choice(words)

def display_the_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else: 
            display += "_"
    return display

def main():
    secret_word = choose_the_word()
    guessed_letters = []
    attempts = 20
    print("Let's play the Word Guessing Game, Version 2!")
    print(display_the_word(secret_word, guessed_letters))
    while "_" in display_the_word (secret_word, guessed_letters) and attempts > 0:
        guess = input("Please guess a letter! A good letter! ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter.")
            continue 
        if guess in guessed_letters:
            print("You've already picked that letter, my guy! Pick somethin' different!")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("That's correct! Keep guessin'!")
        else:
            print("That's not it, my guy! Keep guessin'!")
            attempts -= 1
    if "_" not in display_the_word(secret_word, guessed_letters):
        print("Good job, my boy! You guessed the whole word!")
    else:
        print("Dang man, you ran out of attempts! The word was..." + secret_word + ".")

if __name__ == "__main__":
    main()
