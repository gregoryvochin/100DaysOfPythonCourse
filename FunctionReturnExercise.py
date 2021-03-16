def format_name(a, b):
    first_name = a.title()
    last_name = b.title()

    full_name = f"{first_name} {last_name}"

    return full_name

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

print(format_name(first_name, last_name))
