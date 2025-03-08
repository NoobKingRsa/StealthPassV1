import random
import string
import time
import os

# Function to generate the password
def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to print text with color
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Title and loading screen with color
def show_title():
    print_colored("\n===============================================", "32")
    print_colored("              StealthPass - Password Generator", "32")
    print_colored("===============================================", "32")
    time.sleep(1)

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

# Function to suggest stronger passwords
def suggest_stronger_password(password):
    suggestions = []
    if not any(char.isupper() for char in password):
        suggestions.append("Add uppercase letters.")
    if not any(char.isdigit() for char in password):
        suggestions.append("Include digits.")
    if not any(char in string.punctuation for char in password):
        suggestions.append("Include special characters.")
    
    if not suggestions:
        return "Your password is already strong!"
    else:
        return "To make your password stronger, consider: " + ", ".join(suggestions)

# Stylish prompts with formatted responses
def ask_for_input(prompt, default_value, valid_responses=None):
    while True:
        user_input = input(prompt + f" (default {default_value}): ").strip() or default_value
        if valid_responses:
            if user_input.lower() in valid_responses:
                return user_input.lower()
            else:
                print_colored(f"Invalid input! Please respond with one of: {', '.join(valid_responses)}", "31")
        else:
            return user_input

# Save the password to a file
def save_password_to_file(password):
    file_name = "passwords.txt"
    with open(file_name, "a") as file:
        file.write(password + "\n")
    print_colored(f"Password saved to {file_name}.", "34")

# Display password history
def show_password_history():
    file_name = "passwords.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            print_colored("\nPrevious Passwords Generated:", "33")
            for line in lines[-5:]:
                print_colored(line.strip(), "36")
    else:
        print_colored("No previous passwords saved yet.", "31")

# Main menu
def main_menu():
    show_title()
    print_colored("1. Generate New Password", "33")
    print_colored("2. Test Password Strength", "33")
    print_colored("3. View Password History", "33")
    print_colored("4. Exit", "33")
    
    choice = ask_for_input("Please choose an option", "1", valid_responses=["1", "2", "3", "4"])
    
    return choice

# Main function to execute the program
def main():
    while True:
        choice = main_menu()

        if choice == "1":
            # Password generation
            length = int(ask_for_input("Enter password length", 12, valid_responses=None))
            use_upper = ask_for_input("Include uppercase letters?", "y", valid_responses=["y", "n"]) == "y"
            use_digits = ask_for_input("Include digits?", "y", valid_responses=["y", "n"]) == "y"
            use_special = ask_for_input("Include special characters?", "y", valid_responses=["y", "n"]) == "y"

            print_colored("\nGenerating password...\n", "33")
            time.sleep(2)

            password = generate_password(length, use_upper, use_digits, use_special)
            strength = check_password_strength(password)

            print_colored("\nGenerated Password: ", "34")
            print_colored(password, "36")
            print_colored(f"\nPassword Strength: {strength}", "33")

            # Ask if user wants to save the password
            save_choice = ask_for_input("\nDo you want to save this password to a file?", "y", valid_responses=["y", "n"])
            if save_choice == "y":
                save_password_to_file(password)

        elif choice == "2":
            # Test password strength
            password = input("\nEnter the password to test its strength: ").strip()
            strength = check_password_strength(password)
            print_colored(f"\nPassword Strength: {strength}", "33")

            # Suggest stronger password if weak or medium
            if strength != "Strong":
                suggestions = suggest_stronger_password(password)
                print_colored(suggestions, "31")

        elif choice == "3":
            # Show password history
            show_password_history()

        elif choice == "4":
            # Exit
            exit_confirmation = ask_for_input("Are you sure you want to exit? (Y/N)", "y", valid_responses=["y", "n"])
            if exit_confirmation == "y":
                print_colored("\nThank you for using StealthPass. Exiting now...", "32")
                break
            else:
                continue

# Run the main function
if __name__ == "__main__":
    main()