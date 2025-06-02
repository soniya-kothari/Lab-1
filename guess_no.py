# guess_number.py - Guess the number game

import random

def guess_game():
    number = random.randint(1, 50)
    attempts = 0

    print("Guess a number between 1 and 50.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_game()
