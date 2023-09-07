phrase = input("Enter a phrase: ")
words = phrase.split()
a = " "

for i in words:
    a = a + str(i[0].upper())
print(a)