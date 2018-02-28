a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_list = []

for x in a:
  if x not in my_list:
    my_list.append(x)

for k in b:
  if k not in my_list:
    my_list.append(k)

new_list = sorted(my_list)

print(new_list)