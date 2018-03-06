
print("Let's Check if a word is a palindrome.")

word = (input("Enter a word: "))

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

str1 = word.lower()
str2 = reverse(str1)


if str1 == str2:
  print('Yes')
else:
  print('No')


