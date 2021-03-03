print("Welcome to the BMI Calculator.")

mass = float(input("Please enter your weight in Kilograms: "))
height = float(input("Please enter your height in Metres: "))

bmi = (mass / height ** 2)

roundedBmi = round(bmi, 2)

print(roundedBmi)
