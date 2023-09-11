# most female names in polish ends with "a"
# that is why if statement checks the last letter on input name is "a"

name = input("Enter name: ")
letters = []
letters.extend(list(name))
# print(letters)
# print(letters[-1])
if letters[-1] == "a":
    print("Hello Mrs " + name + "! I hope You have a wonderful day.")
else:
    print("Hello Mr " + name + "! I hope You have a wonderful day.")
