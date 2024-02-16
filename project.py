# Project for Exam

# Guess the number 

import random

def guess_the_number():
    # რანდომის გამოყენებით გენერირება ციფრების 1 დან 20ის ჩათვლით.
    secret_number = random.randint(1, 20)
    
    # მაქსიმალური ცდის რაოდენობა
    max_attempts = 7
    # აქ ვინახავთ ცდების რაოდენობას
    attempts = 0
    
    print("Welcome to Guess the Number","\nChoose number from 1 to 20?")
    
    # ეს ციკლი გვჭირდება იმისთვის რომ სადამ მაქსიმალური მცდელობა მეტი იქნება 0 ზე, გამოვიყენოთ ჩვენი ცდის რაოდენობა.
    while attempts < max_attempts:
            try:
                #თუ თამაშის დამთავრება გსურს exit ქომენდით დავასრულებთ თამაშს
                user_input = input("Enter your guess (between 1 and 20), or type 'exit' to end the game: ")
                if user_input.lower() == 'exit':
                    return
                guess = int(user_input)
                if guess < 1 or guess > 20:
                    print("Please enter a number between 1 and 20.")
                    continue
            except ValueError:
                print("Please enter a valid number or type 'exit' to end the game.")
                continue
            # თუ ისეთი ციფრი შეიყვანა რაც მოცემული არაა 1 დან 20 ის ჩათვლით ის 1 ცდა უკან გიბრუნდება.
            attempts += 1   
            #იუზერისგან გადაცემული ინფუთ რიცხვების მიხედვით გვეუბნება უფრო მაღალი ჩავწეროთ თუ დაბალი.
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

