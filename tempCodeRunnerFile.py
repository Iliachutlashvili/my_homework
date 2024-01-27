
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