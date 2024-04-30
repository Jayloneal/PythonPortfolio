import random

def make_the_secret_code():
    new_edition = ['R,', 'B', 'R', 'M', 'R', 'J'] # Members of New Edition: Ronnie, Bobby, Ricky, Mike, Ralph and Johnny too.
    secret_code = random.sample(new_edition, 4) # Generate a random code from 4 members
    return  secret_code

def test_the_guess(secret_code, guess): 
    exact_matches = 0
    member_matches = 0
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            exact_matches +=1
        elif guess[i] in secret_code:
            member_matches += 1
        return exact_matches, member_matches

def main():
    print("Let's play Brainiac!")
    print("Members of New Edition: R - Ronnie, B - Bobby, R - Ricky, M - Mike, R - Ralph, J - Johnny")
    print("Do yo' absolute best...to guess the secret code in as few attempts as possible.")
    secret_code = make_the_secret_code()
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        guess = input("\nEnter your guess(four members, absolutely no spaces): ").upper()
        if len(guess) != 4 or not all(member in 'RBRMRJ' for member in guess):
            print('Bad entry! Please give a good guess.')
            continue
        attempts += 1
        exact_matches, member_matches = test_the_guess(secret_code, guess)
        print(f"Attempt {attempts}: {guess} - Exact Matches: {exact_matches}, Member matches: ,{member_matches}")
        if exact_matches == 4:
            print("Congrats, my boy! You guessed the secret code!")
            break 
    if attempts == max_attempts and exact_matches != 4:
        print(f"\nDang, man! You ran outta attempts. The secre code was {secret_code}.")

if  __name__ == "__main__":
    main()
