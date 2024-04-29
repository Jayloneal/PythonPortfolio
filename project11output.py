import time

def start_typing_test(text):
    """
    Starts the typing test with the given text.
    :param text: str
    :return: None
    """
    print("Typing test starts now. Type the following text as fast as you can:")
    print(text)
    
    # Wait for user to press Enter to start the timer
    input("Press Enter when you are ready to start...\n")
    start_time = time.time()
    
    # Get the user input
    typed_text = input("Start typing:\n")

    end_time = time.time()
    time_taken = end_time - start_time

    # Calculate words typed and accuracy
    word_count = len(typed_text.split())
    accuracy = (sum(typed_text[i] == text[i] for i in range(min(len(typed_text), len(text)))) / len(text)) * 100

    # Calculate WPM
    wpm = (word_count / time_taken) * 60
    
    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"WPM: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

def main():
    sample_text = "I believe the children are our future. Teach them well and let them lead the way."
    start_typing_test(sample_text)

if __name__ == '__main__':
    main()
