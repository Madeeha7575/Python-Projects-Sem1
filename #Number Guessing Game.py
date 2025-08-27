#Number Guessing Game

import random
def guessing_game():
    level = input("Enter difficulty level (easy/hard):").lower()
    if(level =="easy"):
        attempts =10
    elif(level == "hard"):
        attempts = 5
    else:
        print("Invalid input.Defaulting to easy.")
        attempts = 10
    print(f"You have {attempts} attempts left.")
    num = random.randint(1,50)

    while attempts >0:
        guess = input("Enter a guess between 1 to 50:")
        if guess.isdigit():
            guess = int(guess)
            if(guess< num):
                print("Guess higher.")
            elif(guess>num):
                print("Guess lower.")
            else:
                print("You guessed it right.")
                return
            attempts -=1
            print(f"You have {attempts} attempts left.")
        else:
            print("Invalid answer.Guess again")
       
    print(f"Game over.Number is {num}")
guessing_game()
