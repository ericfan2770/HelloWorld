birth_year = input("Birth year: ") # return value is always a String
print(type(birth_year))
age = 2019 - int(birth_year) # converts birth_year from a String to an integer
print(type(age))
print(age)

weight_pounds = input("What is your weight in pounds? ")
weight_kilograms = int(weight_pounds) / 2.205
print(weight_kilograms)

# Conversions to other types
# int()
# float()
# bool()
