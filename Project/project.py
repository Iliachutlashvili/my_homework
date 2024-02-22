# # Project for Exam

# # წიგნების მართვის აპლიკაცია

import csv
import re
import pygame
import os

class Book:  #Book კლასი რომელიც გვიბრუნებს წიგნის დასახელბას, ავტორს და გამოსვლის თარიღს
    def __init__(self, title, author, release_date):
        self.title = title
        self.author = author
        self.release_date = release_date

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Release Date: {self.release_date}"

class MagicBook(Book):  # გასართობი კლასი რომელიც შემოიტანს ხალისს ჩვენს ბიბლიოთეკაში :D 
    def __init__(self, title, author, release_date, music_file):
        super().__init__(title, author, release_date)
        self.music_file = music_file
        self.is_playing = False

    def play_music(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False

        
class BookManager: #BookManager კლასი რომელიც გვაძლევს საშუალებას დავამატოთ ან ვნახოთ დამატებული წიგნები.
    def __init__(self):
        self.books = []

    def add_book(self, book):  # როდესაც კოდი ახალი გაშვებულია გვხვდება ცარიელი მასივი სადაც ვინახავ ახლად დამატებულ წიგნებს
        self.books.append(book)

    def show_all_books(self):   # ახლად დამატებული ყველა წიგნის ნახვა
        if not self.books:
            print("No books here Check in Library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self, title):   # წიგნების სერჩის ფუნქცია
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def save_to_csv(self, filename):  # ფაილში შენახვა ახლად დამატებული წინების რომლებსაც ვიღებთ მასივიდან რადგან კოდის დახურვის და ახლიდან გაშვების შემთხვევაში არ დავკარგოთინფორმაცია
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Author', 'Release Date'])
            for book in self.books:
                writer.writerow([book.title, book.author, book.release_date])

    def print_csv_data(self, filename):  # ფაილში შენახული ყველა წიგნის,ავტორის და დროის დაპრინტვა/გამოტანა
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))

def validate_input(prompt, regex_pattern): 
    while True:
        user_input = input(prompt)
        if re.match(regex_pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main():  # მეინი უყურებს ბუქ მენეჯერს და გვაძლევს საშუალებას გადაწყვეტილებისამებრ გამოვიძახოთ ის ფუნქცია რომელიც ჩვენ გვინდა მოცემული ციფრების საშუალებით.
    book_manager = BookManager()

    while True:
        print("\nBook Management System")
        print("1. Add a new book")
        print("2. View Just Added books")
        print("3. Seach Books")
        print("4. Save books in csv file")
        print("5. Enter secret name To get all books from library")
        print("6. Bring The Chaos in Library! ")
        print("7. Stop the Chaos")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':   
            print("Add a New Book:")
            title = validate_input("Enter book title: ", r'^[a-zA-Z0-9\s]+$')
            author = validate_input("Enter author name: ", r'^[a-zA-Z\s]+$')
            release_date = validate_input("Enter release date (YYYY-MM-DD): ", r'^\d{4}-\d{2}-\d{2}$')
            new_book = Book(title, author, release_date)
            book_manager.add_book(new_book)
            print("Book added successfully.")

        elif choice == '2':
            print("All Books:")
            book_manager.show_all_books()

        elif choice == '3':
            title = input("Enter Book name to Search: ")
            book_found = book_manager.search_book(title)
            if book_found:
                print("Book found")
                print(book_found)
            else:
                print("Book Not Found!")

        elif choice == '4':
            filename = input("Enter File name to save books: ")
            book_manager.save_to_csv(filename)
            print("Books saved in Csv file")
        
        elif choice == '5':
            filename = input("Enter file name to print data: ")
            book_manager.print_csv_data(filename)

        elif choice == '6':
            print("Bringing The Chaos in Library!")
            title = "Magic Book"
            author = "Magic Author"
            release_date = "2024-02-17"
            music_file = 'music\chaos.mp3'
            magic_book = MagicBook(title, author, release_date, music_file)
            magic_book.play_music()

        elif choice == '7':
            print("Stopping the Chaos!")
            if 'magic_book' in locals() and magic_book.is_playing:
                magic_book.stop_music()
            else:
                print("Chaos is not happening now.")

        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()