import random

def guessing_game():
    print("\t\t\t\t🎉 Welcome to the Guessing Game! 🎉")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's start the game.")
    
    play_again = 'y'
    
    while play_again.lower() == 'y':
        number_to_guess = random.randint(1, 10)
        attempts = 0
        feedback = ""

        print("\nI'm thinking of a number between 1 and 10.")
        print("Can you guess what it is? Let's find out!")
        
        while True:
            guess = input(f"{feedback}\nEnter your guess: ")

            if not guess.isdigit():
                print("That's not a valid number! Try again.")
                continue

            guess = int(guess)
            
            if guess < 1 or guess > 10:
                print("Out of bounds! Please enter a number between 1 and 10.")
                continue

            attempts += 1

            if guess < number_to_guess:
                feedback = "Too low! 🤔 "
            elif guess > number_to_guess:
                feedback = "Too high! 🙃 "
            else:
                print(f"🎉 Congratulations!, {name}! You guessed the number {number_to_guess} in {attempts} attempts! 🏆")
                break

        play_again = input("\nWould you like to play again? (y/n): ").lower()

        while play_again not in ['y', 'n']:
            play_again = input("Invalid input! Please enter 'y' for yes or 'n' for no: ").lower()

    print(f"\nThanks for playing, {name}! See you next time! 👋")

# Start the game
guessing_game()



