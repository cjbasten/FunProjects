def is_cory_here():
    temp = input("Is Cory here?")
    if temp.lower() == "yes":
        is_cory_here()
    else:
        print("Shit")

is_cory_here()

