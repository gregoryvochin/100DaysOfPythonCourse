userNumber = input("Enter a number to find out if it is even or odd: ")

if userNumber.isdigit():
    userNumber = int(userNumber)
    if userNumber % 2 == 0:
        print(f"{userNumber} is an even number.")
    elif userNumber % 2 == 1:
        print(f"{userNumber} is an odd number.")
    else:
        print("Uh...")
else:
    print("You have not entered a number.")
