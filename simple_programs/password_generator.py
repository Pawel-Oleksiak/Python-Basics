import random

# gather all possible characters for the password
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!@#$%^&*()'
numbers = '0123456789'
all = lower + upper + symbols + numbers

# personalize the password
length = int(input("How long should your password be?\n>> "))
print("What characters would you like to use?")
print("Possible options:\n"
      "1. All characters (letters upper and lower case, symbols and numbers),\n"
      "2. Lower case letters, numbers and symbols,\n"
      "3. Upper case letters, numbers and symbols,\n"
      "4. All letters and symbols,\n"
      "5. All letters and numbers.")
choice = input(">> ")

# randomize loop to create password based on user input
password = ""

if choice == '1':
    for _ in range(length):
        password = "".join([password, random.choice(all)])
elif choice == '2':
    for _ in range(length):
        password = "".join([password, random.choice(lower + numbers + symbols)])
elif choice == '3':
    for _ in range(length):
        password = "".join([password, random.choice(upper + numbers + symbols)])
elif choice == '4':
    for _ in range(length):
        password = "".join([password, random.choice(lower + upper + symbols)])
elif choice == '5':
    for _ in range(length):
        password = "".join([password, random.choice(lower + upper + numbers)])
else:
    print("That is not an option.")

# print out the outcome
print("Your randomly generated password is: " + password)