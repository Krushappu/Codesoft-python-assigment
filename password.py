import random
import string

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        print("Invalid complexity level. Please choose 'easy', 'medium', or 'hard'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    while True:
        length = int(input("Enter the desired password length: "))
        complexity = input("Enter the complexity level ('easy', 'medium', or 'hard'): ")

        password = generate_password(length, complexity)
        if password:
            print("Generated Password:", password)

        try_again = input("Generate another password? (yes/no): ")
        if try_again.lower() != "yes":
            print("Goodbye!")
            break
