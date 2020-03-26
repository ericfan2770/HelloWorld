names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names)
print(names[-2])
print(names[2:])
print(names[2:4])

names[0] = "Jon"
print(names)

# String manipulation and array manipulation are pretty much the same!

print()

# Exercise
numbers = [3, 2, 7, 4, 9]
max = numbers[0]  # but this assumes nums is not empty
for number in numbers:
    if number > max:
        max = number
print(max)
