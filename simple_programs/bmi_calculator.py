# user enter required data
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
height = height/100
bmi = round(weight/(height*height), 2)

# based on user input bmi is calculated and returned to user
print("Your Body Mass Index is", bmi)

# based on bmi, user gets information about potential health issue
if bmi > 0:
    if bmi < 16:
        print("Starvation")
    elif 16 <= bmi <= 16.99:
        print("Severely underweight")
    elif 17 <= bmi <= 18.49:
        print("Underweight")
    elif 18.5 <= bmi <= 24.99:
        print("Healthy weight")
    elif 25 <= bmi <= 29.99:
        print("Overweight")
    elif 30 <= bmi <= 34.99:
        print("First degree obesity")
    elif 35 <= bmi <= 39.99:
        print("Second degree obesity")
    else:
        print("Third degree obesity")
else:
    print("Enter valid data.")