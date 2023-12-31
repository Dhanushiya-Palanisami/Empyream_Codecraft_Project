#RANDOM PASSWORD GENERATOR
import random
import string

def generate_password(words, length=12):
    # Check if the length of the password is valid
    if length < 4:
        return "Password length should be at least 4 characters."

    # Shuffle the input words
    random.shuffle(words)

    # Create a random string of characters for the remaining length
    remaining_length = length - len(''.join(words))
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Combine the shuffled words and random characters
    password = ''.join(words) + random_chars

    return password

def main():
    while True:
        # Get user input words
        user_input = input("Enter words separated by spaces: ")
        words = user_input.split()

        # Get desired password length from the user
        try:
            length = int(input("Enter the desired password length: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")
            continue

        # Check if the password length is valid
        if length < 4:
            print("Password length should be at least 4 characters.")
            continue

        # Generate the password
        password = generate_password(words, length)
        print("Generated Password:", password)

        # Ask the user if they want to generate another password
        another = input("Generate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
