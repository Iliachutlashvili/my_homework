# დავალება 1

PeopleCount = int(input("Person Count: "))
count = 0
details = []
PeopleList = [details]
while (count < PeopleCount):
    count += 1
    name = input("1. Enter name: ")
    lname = input("2. Enter Lastname: ")
    age = int(input("3. Enter your Age: "))
    details.append([name, lname, age])

search = int(input('\nWhich one you need?!: '))
persondetails = details[search]
print(f'Name: {persondetails[0]},\nLastname: {persondetails[1]},\nAge: {persondetails[2]}')

# ---------------------------------------------

# დავალება 2

# name = input("Registration Name: ")
# Pass = input("Registration Password: ")
# Account = []
# if len(Pass) < 8:
#     print('Password is Too short! ')
# if len(name) < 3:
#     print('Name is Too short! ')
# else:
#     print('Registration Succesful! ')
# Account.append([name, Pass])

# name = input("Login name: ")
# Pass = input("Login Password: ")
# for element in Account:
#     if element[0] == name and element[1] == Pass:
#         print('You are logged in')

# ------------------------------------------------------

# დავალება 3


# peoplelist = [['Elon musk', 'CEO And Founder of Tesla'],['Jeff Bezos', 'Founder and Ceo of Amazon'],['Bill Gates', 'Founder and CEO of Microsoft']]


# name = input("Name: ")

# for element in peoplelist:
#     if element[0] == name:
#         print(element[1]) 