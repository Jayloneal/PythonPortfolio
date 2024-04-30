import random

def generate_color_sequence(colors_list, length=4):
    return [random.choice(colors_list) for _ in range(length)]

def get_user_guess(colors_list):
    guess = []
    while len(guess) < 4:
        user_input = input(f"Choose a color from {colors_list}: ").strip()
        if user_input in colors_list:
            guess.append(user_input)
        else:
            print("Bad color, my guy! Try that one again.")
    return guess

def check_match(sequence, guess):
    match_result = {"correct": 0, "misplaced": 0}
    checked_indices = []

    # Check correct positions
    for i, color in enumerate(guess):
        if sequence[i] == color:
            match_result["correct"] += 1
            checked_indices.append(i)

    # Check misplaced colors
    for i, color in enumerate(guess):
        if i not in checked_indices and color in sequence and sequence.count(color) > guess[:i].count(color):
            match_result["misplaced"] += 1
    
    return match_result

def main():
    colors_list = ['black', 'navy blue', 'gray', 'silver']
    color_sequence = generate_color_sequence(colors_list)
    attempts = 0
    max_attempts = 10

    print("Let's play the 4-Color Match Game!")
    print(f"The objective of this game is to try to guess the correct sequence of {len(color_sequence)} colors. But the thing is... you have {max_attempts} attempts to do it!")
    print("Here are the colors to choose from:", colors_list)

    while attempts < max_attempts:
        guess = get_user_guess(colors_list)
        result = check_match(color_sequence, guess)
        attempts += 1

        if result["correct"] == len(color_sequence):
            print(f"Congratulations, my guy! You've correctly guessed the sequence! And it only took {attempts} tries to do it!")
            break
        else:
            print(f"The correct color & position is... {result}")
            print(f"Correct color, Wrong spot! {result['misplaced']}")
            print(f"These are the attempts that you have left: {max_attempts - attempts}")
    else:
        print(f"Sorry, my boy! You've run outta attempts. The correct sequence was: {color_sequence}")

if __name__ == "__main__":
    main()
