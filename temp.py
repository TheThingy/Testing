import datetime
year = datetime.date.today().year
name = input("State your name: ")
age = int(input("State your age: "))
copies = int(input("Insert amount of copies: "))
futureAge = year - age + 100

result = "\nName: " + name + "\nAge: " + str(age) + "\nYou will be 100 in year: " + str(futureAge)

if copies >= 1:
    print(result * copies)
else:
    print(result)