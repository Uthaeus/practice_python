import time
import random

print("---------This is the guessing game----------")
time.sleep(1)

game = 'y'
while game == 'y':

  turns = 0

  for x in range(1):
    num = random.randint(1, 10)

  guess = int(input("Pick a number between 1 and 10 \n"))

  while guess != num:
    if guess < num:
      print("Your guess is too low")
      turns += 1
    elif guess > num:
      print("Your guess is too high")
      turns += 1

    guess = int(input("Try again\n"))

  if guess == num:
    print("You guessed it!!")

  game = input("Would you like to play again? (y/n)\n")

  if game != 'y':
    print("Thanks for playing!")


  