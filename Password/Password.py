import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired length for the password: "))
            if password_length <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                generated_password = generate_password(password_length)
                print("Generated Password:", generated_password)
                print("Password Strength:", password_strength(generated_password))

                # Ask if the user wants to generate another password
                user_response = input("Do you want to generate another password? (y/n): ").lower()
                if user_response != 'y':
                    break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")
