import random
import string

adjectives = ["Cool", "jolly ", "Brave", "Smart", "Fast", "Sneaky", "Strong", "Loyal"]
nouns = ["luna ", "krish", "Eagle", "Panther", "Wolf", "Shark", "Fox", "Hawk"]

def generate_username(include_numbers, include_special_chars, length=None):
   
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if include_numbers:
        number = ''.join(random.choices(string.digits, k=3))
        username += number

    if include_special_chars:
        special_char = random.choice(string.punctuation)
        username += special_char

    if length and len(username) > length:
        username = username[:length]

    return username

def save_to_file(usernames, filename="usernames.txt"):
    """Saves a list of usernames to a file."""
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}.")

def main():
    print("Welcome to the Random Username Generator!")
    usernames = []

    while True:
        print("\nOptions:")
        print("1. Generate a username")
        print("2. Save usernames to file")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
            include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            
            try:
                length = int(input("Enter maximum username length (or press Enter for no limit): ") or 0)
                length = length if length > 0 else None
            except ValueError:
                print("Invalid length input. No limit will be applied.")
                length = None

            username = generate_username(include_numbers, include_special_chars, length)
            print(f"Generated Username: {username}")
            usernames.append(username)

        elif choice == "2":
            if usernames:
                save_to_file(usernames)
            else:
                print("No usernames to save.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()