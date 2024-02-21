# # დავალება 1

# def writer():
#     with open('user_input.txt', 'w') as file:
#         while True:
#             user_input = input("Enter text (type 'enough' to stop): ")
#             if user_input.lower() == 'enough':
#                 break
#             file.write(user_input + '\n')

# writer()

# --------------------------------------------------------------------------------

# # დავალება 2
# import os

# def search_folder():
#     folder_location = input("Enter the folder location: ")
#     file_name = input("Enter the file name: ")

#     file_path = os.path.join(folder_location, file_name)

#     try:
#         with open(file_path, 'w') as file:
#             print(f"File '{file_name}' created at '{folder_location}'")

#         print("\nFiles in the directory:")
#         for file in os.listdir(folder_location):
#             if os.path.isfile(os.path.join(folder_location, file)):
#                 print(file)

#     except OSError as e:
#         print(f"Error: Unable to create the file - {e}")

# search_folder()

# # ეს დავალება ცოტა გამიჭირდა და მოძიების საშუალებით დავწერე რეალურად. მესმის რო დაგუგვლაც რო შეგვიძლია ოქეია მარა ისეთი შთაბეჭდილება მრჩება
# # ჩემით რო არ ვწერ, საერთოდ გაგებაში არ ვარ :დ რო ვუყურებ კოდს კი ვხვდები რა სად როგორ, მარა აი ჩემით მიჭირს გახსენება რაღაცეების და წერა დამოუკიდებლად.