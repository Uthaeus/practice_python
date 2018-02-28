
print("-------Odd or Even------")


num = int(input("Enter a number: "))

if num % 2 == 0 and num % 4 == 0:
  print('Special message here')
elif num % 2 == 0:
  print("That number is even.")
elif num % 2 == 1:
  print("That number is odd.")

