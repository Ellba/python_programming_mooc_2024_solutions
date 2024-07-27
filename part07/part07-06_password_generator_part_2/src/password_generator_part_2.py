import secrets
import string

def generate_strong_password(length: int, numbers: bool, special_characters: bool) -> str:
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    special_chars = "!?=+-()#"
    char_pool = string.ascii_lowercase
    password_chars = [secrets.choice(string.ascii_lowercase)]

    # Include at least one number if requested
    if numbers:
        password_chars.append(secrets.choice(string.digits))
        char_pool += string.digits

    # Include at least one special character if requested
    if special_characters:
        password_chars.append(secrets.choice(special_chars))
        char_pool += special_chars

    # Fill the rest of the password length
    while len(password_chars) < length:
        password_chars.append(secrets.choice(char_pool))

    # Shuffle the characters to ensure randomness
    secrets.SystemRandom().shuffle(password_chars)
    
    return ''.join(password_chars)

if __name__ == "__main__":
    try:
        for i in range(10):
            print(generate_strong_password(12, True, True))  # Example: 12 characters long, with numbers and special characters
    except ValueError as e:
        print(f"Error: {e}")
