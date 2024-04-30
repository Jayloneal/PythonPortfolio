import random

def choose_word():
    words = ["octopus", "tractor", "fork", "wheel", "plate", "golf", "spider", "cactus", "television", "chicken", "sky", "cloud", "dinner", "stake", "balloon", "work", "home", "freeze", "marble", "fish", "tax", "safe", "camera", "cookie", "makeup", "hair", "trailer", "ditch", "camel", "sand", "box", "fry", "river", "moon", "eyes", "clothing", "radio", "strap", "table", "legs"]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 20
    print("Welcome to the Hangman Game, Version 2!")
    print(display_word(secret_word, guessed_letters))
    while "_" in display_word(secret_word, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess)!= 1 or not guess.isalpha():
            print("Please pick a letter, my guy.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter, big dawg.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("You guessed correctly, my guy! Keep guessin'!")
        else:
            print("You guessed incorrectly, my guy! Keep guessin'!")
            attempts -= 1
        print(display_word(secret_word, guessed_letters))
        print("Attempts remaining: " + str(attempts))
    if "_" not in display_word(secret_word, guessed_letters):
        print("Congratulations, my guy! You guessed the whole word.")
    else:
        print("Sorry, my guy! You've ran outta attempts. The word was " + secret_word + ".")

if __name__ == "__main__":
    main()
