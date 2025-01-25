# Word Counter Project
# This program counts the number of words in a given sentence or paragraph entered by the user.

def count_words(text):
    """
    This function takes a string as input and returns the number of words in the string.
    Words are considered to be sequences of characters separated by spaces.
    """
    # Split the text into words using whitespace as a delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    """
    Main function to execute the Word Counter program.
    Handles user input, word counting, and displaying the result.
    """
    print("Welcome to the Word Counter!")
    print("Enter a sentence or paragraph to find out how many words it contains.")
    
    while True:
        # Prompt the user for input
        user_input = input("\nPlease enter your text (or type 'exit' to quit): ").strip()
        
        # Check if the user wants to exit the program
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter! Goodbye!")
            break
        
        # Check for empty input
        if not user_input:
            print("Error: You entered an empty input. Please try again.")
            continue
        
        # Count the words in the input
        word_count = count_words(user_input)
        
        # Display the word count
        print(f"The number of words in your input is: {word_count}")

# Execute the main function
if __name__ == "__main__":
    main()
