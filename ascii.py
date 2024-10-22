import pyfiglet
import os

def clear_console():
    """Clears the console to keep things tidy."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    """Displays the title of the program."""
    title = pyfiglet.figlet_format("made by scarfce")
    print(title)

def welcome():
    """Shows a welcome message and instructions."""
    print("welcome to my ascii art generator")
    print("type 'exit' to quit anytime.")

def choose_font():
    """Prompts the user to select a font style."""
    print("pick a font:")
    print("1. standard")
    print("2. slant")
    print("3. digital")  # Changed font option
    print("4. block")
    print("5. bubble")
    return input("font choice (1-5): ").lower()

def main():
    while True:
        clear_console()
        print_title()
        welcome()

        font_choice = choose_font()

        if font_choice == 'exit':
            print("thanks for using the generator! bye!")
            break

        # Map choices to actual font names
        fonts = {
            '1': 'standard',
            '2': 'slant',
            '3': 'digital',
            '4': 'block',
            '5': 'bubble'
        }
        
        selected_font = fonts.get(font_choice, 'standard')  # Default to standard if invalid

        user_text = input("what do you want in ascii art? ")

        if user_text.lower() == 'exit':
            print("thanks for using the generator! bye!")
            break
        
        clear_console()

        try:
            # Generate ASCII art using the selected font
            ascii_art = pyfiglet.figlet_format(user_text, font=selected_font)
            print(ascii_art)
        except Exception as e:
            print(f"uh-oh! something went wrong: {e}")

        input("press enter to continue...")  # Wait for the user to continue

if __name__ == "__main__":
    main()
