def clear():
    print("\n" * 40)

def user_entry():
    
    i = input("What is your name?: ")
    
    input_dict[i] = input("What's your bid?: ")

more = True

input_dict = {}

print("Welcome to the silent auction program.")

user_entry()

print(input_dict)

while more is True:

    cont = (input("Are there any other bidders? Type 'yes' or 'no'.\n"))
    
    if cont == "yes":
        clear()

        user_entry()

        print(input_dict)

    elif cont == "no":

        more = False

    else:

        print("nope")

highest_bid = 0
hightest_key = ""

for key in input_dict:
    current_bid = input_dict[key]
    current_bid = int(current_bid)
    
    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_key = key
        


print(f"the highest bid was ${highest_bid} by {highest_key}")
