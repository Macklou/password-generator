import random
import string

def generate_password(length, use_numbers=True, use_lowercase=True, use_uppercase=True, use_symbols=True, use_spaces=True):
    characters = ''
    
    if use_numbers:
        characters += string.digits
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation
    if use_spaces:
        characters += ' '

    if not characters:
        print("Error: Please select at least one option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("Options:")
    print("1. Numbers")
    print("2. Lowercase letters")
    print("3. Uppercase letters")
    print("4. Symbols")
    print("5. Spaces")

    options = {
        1: "use_numbers",
        2: "use_lowercase",
        3: "use_uppercase",
        4: "use_symbols",
        5: "use_spaces",
    }

    selected_options = [options[int(input(f"Include option {i}? (1/0): "))] for i in range(1, 6)]

    password = generate_password(8, *selected_options)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()