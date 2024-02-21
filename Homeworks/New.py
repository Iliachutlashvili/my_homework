import json
from datetime import datetime

class User:
    def __init__(self, username, file_path):
        self.username = username
        self.file_path = file_path
        self.active = True

    def upload_message(self, message, date):
        with open("data.json") as file:
            data = json.load(file)

        new_data = {"username": self.username, "message": message, "date": date[:-7]}
        data["Chat"].append(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=5)

    def write_message(self):
        if self.active:
            new_message = input(f"{self.username}: ")
            if new_message.lower() == "quit":
                new_message = f"{self.username} left the chat..."
                print(new_message)
                self.active = False

            date = str(datetime.now())
            #add message to json file
            self.upload_message(new_message, date)
            
    def print_chat(self):
        with open(self.file_path) as file:
            data = json.load(file)
            for chat_print in data['Chat']:
                print(f"Date: {chat_print['date']}\n{chat_print['username']}: {chat_print['message']}")



user1 = User("Elene", "data.json")
user2 = User("Davit", "data.json")


# while user1.active or user2.active:
#     user1.write_message()
#     user2.write_message()

user1.print_chat()

# Date: 2024.2.12
# Elene: How are you?