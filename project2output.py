#Welcome Message!

print("Welcome to Madlibs!")
print("Please type the words if you want to play:")

#What they'll type in
adjective1 = input("Adjective: ")
noun1 = input("First noun: ")
past_tense_verb = input("Past tense verb: ")
adverb = input("Adverb: ")
adjective2 = input("Another adjective: ")
noun2 = input("Second noun: ")
noun3 = input("Third noun: ")
adjective3 = input("Third adjective goes here: ")
verb = input("Verb: ")
adverb2 = input("Another adverb: ")
past_tense_verb2 = input("Another past tense verb: ")
adjective4 = input("Last adjective! I promise: ")

#Write the story
story = f"Today, I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree. " \
        f"He {past_tense_verb} {adverb} through the large tunnel that led to its {adjective2} {noun2}. " \
        f"I got some peanuts and passed them through the cage to a gigantic gray {noun3} " \
        f"towering above my head. Feeding that animal made me hungry. " \
        f"I went to get a {adjective3} scoop of ice cream. It filled my stomach. " \
        f"Afterwards, I had to {verb} {adverb2} to catch our bus. " \
        f"When I got home, I {past_tense_verb2} my mom for a {adjective4} day at the zoo. "

# Display the story
print("\nHere's yo' story!")
print(story)
