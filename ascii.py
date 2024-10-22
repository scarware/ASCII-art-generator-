import pyfiglet
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    title = pyfiglet.figlet_format("made by scarfce")
    
    while True:
        clear_console()  # Clear the console at the start of each loop
        print(title)  # Print the watermark
        print("welcome to my ASCII art generator")
        print("type 'exit' to quit.")

        user_input = input("enter text to convert to ascii art: ")
        
        if user_input.lower() == 'exit':
            print("exiting the program.")
            break
        
        # Clear the console for ASCII art display
        clear_console()

        # Generate ASCII art
        ascii_art = pyfiglet.figlet_format(user_input)
        print(ascii_art)

        input("press enter to continue...")  # Wait for user input before clearing the console again

if __name__ == "__main__":
    main()
