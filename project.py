# Project for Exam

# Guess the number 

import random

def guess_the_number():
    # რანდომის გამოყენებით გენერირება ციფრების 1 დან 20ის ჩათვლით.
    secret_number = random.randint(1, 20)
    
    # მაქსიმალური ცდის რაოდენობა
    max_attempts = 7
    attempts = 0
    
    print("Welcome to Guess the Number","\nChoose number from 1 to 20?")
    
    while attempts < max_attempts:
        try:
            user_input = input("Enter your guess (between 1 and 100), or type 'exit' to end the game: ")
            if user_input.lower() == 'exit':  #თუ თამაში მოგბეზრდა და დამთავრება გსურს exit ქომენდით დავასრულებთ თამაშს
                return
            guess = int(input("Enter your guess (between 1 and 20): "))
            if guess < 1 or guess > 20:
                print("I Said from 1 to 20! .")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()