numbers = [5, 2, 1, 7, 4]
numbers.append(20)  # adds new number to end of list
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 9)  # like add method for Lists in Java
print(numbers)
numbers.insert(3, 8)
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.remove(2)  # removes the element to be removed
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)
print()

numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))  # returns index of first occurrence of argument (like Java indexOf)
# print(numbers.index(10))

# can also use in
print(5 in numbers)
print(10 in numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
print()

numbers2 = numbers.copy()  # independent copy of numbers
numbers.append(10)

print(numbers2)
print()

# Exercise
nums = [2, 2, 3, 3, 5, 5, 1, 1, 2, 3]
uniques = []

for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)
