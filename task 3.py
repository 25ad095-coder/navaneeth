# Password Generator

import random
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Error: Password length must be greater than 0.")

    else:
        # Character sets
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        # Combine all characters
        characters = letters + numbers + symbols

        # Generate password
        password = ""

        for i in range(length):
            password += random.choice(characters)

        # Display password
        print("\nGenerated Password:", password)

except ValueError:
    print("Error: Please enter a valid number.")
