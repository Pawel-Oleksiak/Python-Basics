print("Hello! What would you like to recalculate today?\n"
      "1. Celsius -> Fahrenheit\n"
      "2. Fahrenheit -> Celsius\n"
      "3. Celsius -> Kelvin\n"
      "4. Kelvin -> Celsius\n"
      "5. Fahrenheit -> Kelvin\n"
      "6. Kelvin -> Fahrenheit")
choice = input(">> ")
temperature = float(input("Enter the temperature to recalculate: "))


def celsius_fahrenheit():
    return round(2 * (temperature - 0.1 * temperature) + 32, 2)


def fahrenheit_celsius():
    return round(((temperature - 32) / 2) * 1.1, 2)


def celsius_kelvin():
    return round(temperature + 273.15, 2)


def kelvin_celsius():
    return round(temperature - 273.15, 2)


def fahrenheit_kelvin():
    return round((temperature - 32) * 5 / 9 + 273.15, 2)


def kelvin_fahrenheit():
    return round((temperature - 273.15) * 1.8 + 32, 2)


if choice == "1":
    print(temperature, "degrees Celsius equals to", celsius_fahrenheit(), "degrees Fahrenheit.")
elif choice == "2":
    print(temperature, "degrees Fahrenheit equals to", fahrenheit_celsius(), "degrees Celsius.")
elif choice == "3":
    print(temperature, "degrees Celsius equals to", celsius_kelvin(), "degrees Kelvin.")
elif choice == "4":
    print(temperature, "degrees Kelvin equals to", kelvin_celsius(), "degrees Celsius.")
elif choice == "5":
    print(temperature, "degrees Fahrenheit equals to", fahrenheit_kelvin(), "degrees Kelvin.")
elif choice == "6":
    print(temperature, "degrees Kelvin equals to", kelvin_fahrenheit(), "degrees Fahrenheit.")
else:
    print("Not an option. Try again.")

# --------------- OLD VERSION OF TEMPERATURE RECALCULATOR ---------------
# print("Would you like to recalculate the temperature from Celsius to Fahrenheit?")
# choice = input("Yes / No\n").lower()
# if choice == "yes":
#     temp_celsius = float(input("Enter temperature in Celsius: "))
#     temp_fahrenheit = 2 * (temp_celsius - 0.1 * temp_celsius) + 32
#     print(temp_celsius, "degrees Celsius equals to", temp_fahrenheit, "degrees in Fahrenheit.")
# elif choice == "no":
#     print("Would you like to recalculate the temperature from Fahrenheit to Celsius?")
#     choice = input("Yes / No\n").lower()
#     if choice == "yes":
#         temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         temp_celsius = ((temp_fahrenheit - 32) / 2) * 1.1
#         print(temp_fahrenheit, "degrees Fahrenheit equals to", temp_celsius, "degrees in Celsius.")
#     elif choice == "no":
#         print("Would you like to recalculate the temperature from Celsius to Kelvin?")
#         choice = input("Yes / No\n").lower()
#         if choice == "yes":
#             temp_celsius = float(input("Enter temperature in Celsius: "))
#             temp_kelvin = temp_celsius + 273.15
#             print(temp_celsius, "degrees Celsius equals to", temp_kelvin, "degrees Kelvin.")
#         elif choice == "no":
#             print("Would you like to recalculate the temperature from Kelvin to Celsius?")
#             choice = input("Yes / No\n").lower()
#             if choice == "yes":
#                 temp_kelvin = float(input("Enter temperature in Kelvin: "))
#                 temp_celsius = round(temp_kelvin - 273.15, 2)
#                 print(temp_kelvin, "degrees Kelvin equals to", temp_celsius, "degrees Celsius.")
#             else:
#                 print("Maybe next time.")
# else:
#     print("Not an option.")
