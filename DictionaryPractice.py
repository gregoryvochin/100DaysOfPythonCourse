more = True

input_dict = {}

while more is True:

    cont = (input("Are there more entries? \n"))
    if cont == "yes":

        i = input("")
    
        input_dict[i] = input("")

        print(input_dict)

    elif cont == "no":

        more = False

    else:

        print("nope")
