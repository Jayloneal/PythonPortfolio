def introduction():
    print("During your car ride, you come across a road with two streets.")
    first_choice()

def first_choice():
    choice = input("Do you go left or right? (left/right): ").lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("That's not a good choice. Choose again. Remember, you can only go left or right.")
        first_choice()

def left_path():
    print("You're riding down the street, but this is the long way! You see an opportunity to take this expressway, which will take you all the way home!")
    choice = input("Do you wanna take the expressway home? (yes/no): ").lower()
    if choice == "yes":
        take_the_expressway_home()
    else: 
        print("You chose to take the long way home! It took twenty - five minutes to get back, but you made it back in one piece!")

def right_path():
    print("You're taking the shortcut back, but you hit a nail and it flattened your tire!")
    choice = input("Do you call someone from Roadside Assistance to help? (yes/no): ").lower()
    if choice == "yes":
        print("Someone from Roadside appears, removes the nail from the tire and inflates the tire to its proper PSI. You then ride home, relieved.")
    else:
        print("You call someone to tow the car to your house, have someone drop you off and you pay for the towing service.")

def take_the_expressway_home():
    print("You get stuck in traffic and it takes hours for you to get out of it. However, you notice an exit that will take you back home, but you may have to turn around.")
    choice = input("Do you take the exit? (yes/no): ").lower()
    if choice == "yes":
        print("You take the exit, turn around and ride the expressway all the way back home on the opposite lane!")
    else:
        print("You remain stuck in traffic. Game over!")

if __name__ == "__main__":
    introduction()
