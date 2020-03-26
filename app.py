# function: container with a few lines of code for a specific purpose
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print('Welcome aboard')


print("Start")
greet_user("Fan", "Eric")  # positional arguments: their position/order matters
print("Finish")

print()

# keyword arguments: their order does NOT matter
greet_user(last_name="Fan", first_name="Eric")  # keyword arguments, helps with readability sometimes

# calc_cost(total=50, shipping=5, discount=0.1)  # can be difficult to read

# greet_user(first="John", "Smith") cannot mix keyword and positional args unless keyword is after positional args
greet_user("John", last_name="Smith")
