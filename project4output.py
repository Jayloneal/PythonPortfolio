def get_user_choice(options):
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}") 
    while True:
        user_choice = input("Enter a number! Any number at all!: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if 1 <= user_choice <= len(options):
                return user_choice
        print("Wrong answer, my guy! Try that thang again!")
        
def main():
    questions = [
        {
            "question": "How many letters are in the alphabet?",
            "options": ["26", "25", "13", "27"],
            "answer": 3 #13. "There are thirteen letters in the sentence "the alphabet".
        },
        {
            "question": "If you were in a race and you passed someone who was in third place, what place would you be in?",
            "options": ["1st", "2nd", "3rd", "4th"],
            "answer": 3 #3rd. You would be in third place.
        },
        {
            "question": "What's something that has a head, a tail and no paws?",
            "options": ["Lettuce", "cabbage", "quarter", "onion"],
            "answer": 3 #quarter. A quarter has a head side and a tail side, but no paws. A quarter is not an animal.
        }
    
    ]

    score  = 0
    for q in questions:
        print(q["question"])
        user_choice = get_user_choice(q["options"])
        if user_choice == q["answer"]:
            print("Ay! You got it right, my guy! You're invited to the barbecue!")
            score += 1
    else:
        print("You lost yo' spot at the cookout, my guy!")
    print()

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
