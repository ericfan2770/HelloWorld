temperature = 30

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Exercise 1
name = input("What is your name? ")
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

# Exercise 2
weight = int(input("Weight: "))
weight_type = input("(L)bs or (K)g: ")
if weight_type.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilograms")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
