print("Welcome!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
year = (100 - age) + 2018

num = int(input("Enter any number you'd like: "))
message = "Well hello there, {0}. You say that you are {1}, which means that in {2} you will be 100 years old.".format(name, age, year) + "\n"

print(num * message)