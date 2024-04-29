### 1. Import Required Modules

#First, import the required modules. We'll use `random` for generating random symbols on each spin.

import random 

### 2. Define the Symbol Pool

#Define a list containing our symbols. Each symbol can be represented as a string.

symbols = ["Cherry", "Lemon", "Orange", "Bell", "Bar", "7"]

### 3. Create a Function to Spin the Reels

#This function will simulate spinning the reels of the slot machine. It will randomly choose a symbol for each reel.

def spin_reels(symbols):
    return random.choice(symbols), random.choice(symbols), random.choice(symbols)

### 4. Determine the Outcome

#Let's keep the winning condition simple for this example: the player wins if all three symbols are the same. Create a function to check the result.

def check_win(reel_outcome):
    symbol1, symbol2, symbol3 = reel_outcome
    if symbol1 == symbol2 == symbol3:
        return True
    return False

### 5. Main Function to Play the Slot Machine

#Combine everything into a main function where the user can input their bet and spin the reels.

def play_slot_machine():
    input("Press 'Enter' to spin the reels!")
    outcome = spin_reels(symbols)
    print(f"The reel outcomes are... {outcome}")
    if check_win(outcome):
        print("Congratulations, baby bruh! You made bank!")
    else: 
        print("Sorry, big dawg! You lost!")

# Optionally, you can add a feature to let users play again or quit.

### 6. Run the Slot Machine

#Finally, allow the user to play the slot machine by calling the `play_slot_machine` function.

if __name__ == "__main__":
    play_slot_machine()
