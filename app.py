# try block
# try-except blocks are used to handle exceptions that are raised in our programs
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0!")
# if a ValueError occurs, then print
except ValueError:
    print("Invalid value!")

# exit code 0 means program terminated properly
# exception crashes our program
