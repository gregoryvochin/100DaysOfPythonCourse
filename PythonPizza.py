print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y of N: ")

bill = 0

if size == "S":
    bill = 15
    print("Small pizzas are $15")
    if add_pepperoni == "Y":
        bill += 2
        print("Adding pepperoni to a small pizza costs $2")
    
elif size == "M":
    bill = 20
    print("Medium pizzas are $20")
    if add_pepperoni == "Y":
        bill += 3
        print("Adding pepperoni to a medium pizza costs $3")
else:
    bill = 25
    print("Large pizzas are $25")
    if add_pepperoni == "Y":
        bill += 3
        print("Adding pepperoni to a large pizza costs $3")

if extra_cheese == "Y":
    bill += 1
    print("Adding extra cheese to any pizza costs $1")

print(f"Your final bill is {bill}")





