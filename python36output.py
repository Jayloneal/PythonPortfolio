import random

def generate_number():
    return random.sample(range(10), 4)

def check_guess(guess, secret):
    cows = sum(g == s for g, s in zip(guess, secret))
    bulls = sum(g in secret for g in guess) - cows
    return cows, bulls

def play_game():
    secret = generate_number()
    guesses = 0
    while True:
        guess = list(map(int, input("Enter a 4-digit number: ").strip()))
        guesses += 1
        if len(guess) != 4:
            print("Bad guess. Please enter a 4-digit number.")
            continue
        cows, bulls = check_guess(guess, secret)
        print(f"{cows} cow(s), {bulls} bull(s)")
        if cows == 4:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            break

if __name__ == "__main__":
    play_game()
