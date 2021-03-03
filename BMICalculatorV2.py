print("Welcome to the BMI Calculator.")

mass = float(input("Please enter your weight in Kilograms: "))
height = float(input("Please enter your height in Metres: "))

bmi = (mass / height ** 2)

roundedBmi = round(bmi, 2)

if roundedBmi < 18.5:
    print(f"Your BMI is {roundedBmi}, you are underweight.")
elif roundedBmi < 25:
    print(f"Your BMI is {roundedBmi}, you are at a normal weight.")
elif roundedBmi < 30:
    print(f"Your BMI is {roundedBmi}, you are overweight.")
elif roundedBmi < 35:
    print(f"Your BMI is {roundedBmi}, you are obese.")
elif roundedBmi > 35:
    print(f"Your BMI is {roundedBmi}, you are clinically obese.")
else:
    print("Uh...")
