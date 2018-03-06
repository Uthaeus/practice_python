import time



print("*************Welcome to Rock Paper Scissors***************")
time.sleep(2)

game = 'y'
while game == 'y':

  pone = input("Player One choose your weapon: ")
  ptwo = input("Player Two choose your weapon: ")

  p1 = pone.lower()
  p2 = ptwo.lower()

  time.sleep(1)

  if p1 == p2:
    print("It's a draw!")
  elif p1 == 'rock' and p2 == 'paper':
    print("Player 2 wins!")
  elif p1 == 'rock' and p2 == 'scissors':
    print("Player 1 wins!")
  elif p1 == 'paper' and p2 == 'rock':
    print("Player 1 wins!")
  elif p1 == 'paper' and p2 == 'scissors':
    print("Player 2 wins!")
  elif p1 == 'scissors' and p2 == 'rock':
    print("Player 2 wins!")
  elif p1 == 'scissors' and p2 == 'paper':
    print("Player 1 wins!")

  game = input("Would you like to play again? (y/n)\n" )
  if game != 'y':
    print("Thanks for playing")