"""Mini Project: Password Generator"""
import random
import string


def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def ask_yes_no(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"


def main():
    print("=== Password Generator ===")
    while True:
        try:
            length = int(input("Password length (min 6): "))
            if length >= 6:
                break
            print("Too short, try again.")
        except ValueError:
            print("Please enter a number.")

    digits = ask_yes_no("Include digits?")
    symbols = ask_yes_no("Include symbols?")
    print("Your password:", generate_password(length, digits, symbols))


if __name__ == "__main__":
    main()
