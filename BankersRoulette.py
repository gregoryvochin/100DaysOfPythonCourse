import random

patrons = input("Who was dining with us today? Separate by commas please: ")

names = patrons.split(", ")

gun = random.randint(0, len(names)-1)

print(f"{names[gun]} has to pay today!")
