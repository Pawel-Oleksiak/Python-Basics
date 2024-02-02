# Define possible actions
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


# Show the user possible options
print("Welcome to simple Calculator\n"
      "Choose an option:\n"
      "1. Add two numbers\n"
      "2. Subtract two numbers\n"
      "3. Divide two number\n"
      "4. Multiply two numbers")

possibilities = ['1', '2', '3', '4']

while True:
    # Take the input from user
    choice = input("Choose one of available options (1 - 4)\n"
                   ">> ")
    if choice in possibilities:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Enter number.")
            continue

        if choice == '1':
            print("{} + {} = {}".format(x, y, add(x, y)))
        elif choice == '2':
            print("{} - {} = {}".format(x, y, subtract(x, y)))
        elif choice == '3':
            # Since it is not allowed to divide by 0 we have to check if num2 != 0
            try:
                print("{} / {} = {}".format(x, y, divide(x, y)))
            except ZeroDivisionError:
                print("You cannot divide by 0.")
                continue
        elif choice == '4':
            print("{} * {} = {}".format(x, y, multiply(x, y)))
# Lastly we check if user wants to use the program
        cont = input("Would You like to continue using Calculator [Y/N]: ").lower()
        if cont == 'n':
            break
    else:
        print("Invalid input.")
