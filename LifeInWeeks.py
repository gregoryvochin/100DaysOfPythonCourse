print("Welcome to the life in weeks calculator.")

userAge = int(input("Please enter your current age in years: "))

lifeExpectancy = 90

yearsLeft = lifeExpectancy - userAge

daysLeft = yearsLeft * 365

weeksLeft = round(daysLeft / 7)

monthsLeft = round(weeksLeft / 4.345)

print(f"You have {daysLeft} days, {weeksLeft}, and {monthsLeft}.")

