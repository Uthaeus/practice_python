a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

num = int(input("Give me a number: "))

for x in a:
  if x < num:
    new_list.append(x)


print(new_list)
