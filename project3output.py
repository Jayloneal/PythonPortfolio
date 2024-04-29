import random
import time

def generate_question():
    operation = random.choice(['+', '-', '*', '/'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    #For division, see that the second number isn't zero.
    if operation ==  '/':
        num2 = random.randint(1, 10)
    question = f"What is {num1} {operation} {num2}?"
    correct_answer = eval(f"{num1} {operation} {num2}")
    return question, correct_answer
    
def timed_math_challenge(duration=60):
    start_time = time.time()
    end_time = start_time + duration
    score = 0
    
    try: 
        while time.time() < end_time:
            question, correct_answer = generate_question()
            print(question)
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("Ay! You got it right, my guy!")
                score += 1
            else:
                print(f"That's wrong, my guy! This was the correct answer! {correct_answer}.")
            print(f"This is how much time you have: {max(0, int(end_time - time.time()))}")
            print()
    except ValueError:
        print("Please enter a number.")
    except KeyboardInterrupt:
        print("\nMission failed. Ship abandoned.")
    finally:
        print(f"Time's up! Your score is {score}.")
        
if __name__ == "__main__":
    print("Welcome to the Timed Math Challenge!")
    duration = input("Enter the challenge duration in seconds (default is 60): ")
    if duration.isdigit():
        timed_math_challenge(int(duration))
    else:
        timed_math_challenge()
