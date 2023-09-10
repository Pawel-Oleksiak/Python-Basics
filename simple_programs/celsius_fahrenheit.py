print("Would you like to recalculate the temperature from Celsius to Fahrenheit?")
choice = input("Yes / No\n").lower()
if choice == "yes":
    temp_celsius = float(input("Enter temperature in Celsius: "))
    temp_fahrenheit = 2 * (temp_celsius - 0.1 * temp_celsius) + 32
    print(temp_celsius, "degrees Celsius equals to", temp_fahrenheit, "degrees in Fahrenheit.")
elif choice == "no":
    print("Would you like to recalculate the temperature from Fahrenheit to Celsius?")
    choice = input("Yes / No\n").lower()
    if choice == "yes":
        temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        temp_celsius = ((temp_fahrenheit - 32) / 2) * 1.1
        print(temp_fahrenheit, " degrees Fahrenheit equals to", temp_celsius, "degrees in Celsius.")
    else:
        print("Maybe next time.")
else:
    print("Not an option.")