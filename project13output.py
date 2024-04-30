import random 
import string 

def generate_complex_password(length):
    if length < 4:
        raise ValueError("Length must be at least 4 characters.")
    
    # Character sets from which to choose each required character type
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation

    # See that the password is complex by picking from at least one of each category
    password = [
        random.choice(lowers),
        random.choice(uppers),
        random.choice(digits),
        random.choice(specials)
    ]

    #  Fill out the rest of the password with random characters
    all_chars = lowers + uppers + digits + specials
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle to avoid a predictable pattern
    random.shuffle(password)

    # Join shuffled characters into a single string
    return ''.join(password)

# Example Usage
password_length = 12 # Adjust the length as it's needed
password = generate_complex_password(password_length)
print("Generated Complex Password:", password)
