year = int(input("Enter the year to find out if it is a leap year: "))

if (year % 4) == 0 and ((year % 100) == 0 and (year % 400) == 0):
    print(f"{year} is a leap year.")
    
else:
    print(f"{year} is not a leap year.")
