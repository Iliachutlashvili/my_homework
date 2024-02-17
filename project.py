# # Project for Exam

# # Guess the number 

# import random

# def guess_the_number():
#     # რანდომის გამოყენებით გენერირება ციფრების 1 დან 20ის ჩათვლით.
#     secret_number = random.randint(1, 20)
    
#     # მაქსიმალური ცდის რაოდენობა
#     max_attempts = 7
#     # აქ ვინახავთ ცდების რაოდენობას
#     attempts = 0
    
#     print("Welcome to Guess the Number","\nChoose number from 1 to 20?")
    
#     # ეს ციკლი გვჭირდება იმისთვის რომ სადამ მაქსიმალური მცდელობა მეტი იქნება 0 ზე, გამოვიყენოთ ჩვენი ცდის რაოდენობა.
#     while attempts < max_attempts:
#             try:
#                 #თუ თამაშის დამთავრება გსურს exit ქომენდით დავასრულებთ თამაშს
#                 user_input = input("Enter your guess (between 1 and 20), or type 'exit' to end the game: ")
#                 if user_input.lower() == 'exit':
#                     return
#                 guess = int(user_input)
#                 if guess < 1 or guess > 20:
#                     print("Please enter a number between 1 and 20.")
#                     continue
#             except ValueError:
#                 print("Please enter a valid number or type 'exit' to end the game.")
#                 continue
#             # თუ ისეთი ციფრი შეიყვანა რაც მოცემული არაა 1 დან 20 ის ჩათვლით ის 1 ცდა უკან გიბრუნდება.
#             attempts += 1   
#             #იუზერისგან გადაცემული ინფუთ რიცხვების მიხედვით გვეუბნება უფრო მაღალი ჩავწეროთ თუ დაბალი.
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
#                 break
#     else:
#         print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
        
# guess_the_number()


# # ----------------------------------------------------------------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------------------------------------------------------------


# # წიგნების მართვის აპლიკაცია

import csv

class Book:  #Book კლასი რომელიც გვიბრუნებს წიგნის დასახელბას, ავტორს და გამოსვლის თარიღს
    def __init__(self, title, author, release_date):
        self.title = title
        self.author = author
        self.release_date = release_date

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Release Date: {self.release_date}"

class MagicBook(Book):
    def __init__(self, title, author, release_date):
        super().__init__(title, author, release_date)
        print(self.title,"is singing")
    



class BookManager: #BookManager კლასი რომელიც გვაძლევს საშუალებას დავამატოთ ან ვნახოთ დამატებული წიგნები.
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Author', 'Release Date'])
            for book in self.books:
                writer.writerow([book.title, book.author, book.release_date])


class main:
    book_manager = BookManager

    human_input = input("book name: ")
    author_input = input("Author name: ")
    release_date_input = int(input("Release Date: "))
    if human_input == "1":
        new_book = Book(human_input,author_input,release_date_input )
    elif human_input == "2":
        new_book = MagicBook(human_input,author_input,release_date_input)