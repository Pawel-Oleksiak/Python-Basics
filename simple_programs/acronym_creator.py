# user enters phrase
phrase = input("Enter a phrase: ")
words = phrase.split()
a = " "

# program loops through each word separately
for i in words:
    a = a + str(i[0].upper())
print(a)