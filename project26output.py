import random 

# The function for playing the game
def play_game():
    total = 0
    player = random.randint(0, 1)
    name = str(input("Enter the name that they call you in da hood: "))
    # Print welcome message and display
    print("Let's play 100! In '100', each person can choose '1', '2', or '3' to a running total.")
    print("The player whose turn it is when the score is '21' wins!")
    print(f"The total is {total}")
    while True:
        if player == 0:
            while True:
                try:
                    choice = int(input("What number are you going to play today? "))
                    if 1 <= choice <= 3:
                        break
                    else:
                        print("Please enter a number between '1' and '3'...")
                except ValueError:
                    print("Wrong choice. Please drop a new number. *Remember, between '1' and '3'.")
        else:
            choice = random.randint(1, 3)
            print(f"Computer plays: ")

        total += choice
        if total >= 100:
            if player == 0:
                print("{name} wins!")
            else:
                print("Computer wins!")
            break

        if  player == 0:
            player = 1
        else:
            player = 0
        print(f"The total is: {total}")

if  __name__ == "__main__":
    play_game()
