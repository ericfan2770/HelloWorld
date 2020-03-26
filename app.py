course = 'Python for Beginners'
print(len(course))  # len is a general purpose function

# Methods belong to a particular class (String methods, Array methods, etc), while
# functions are general purpose (works for many types of objects)

print(course.upper())
print(course.lower())

print(course.find('P'))  # find is like the Java indexOf method
print(course.find('o'))
print(course.find('O'))

print(course.find('Beginners'))  # Returns index of first occurrence of the given String

print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

print('Python' in course)  # like indexOf('Python') != -1
print('python' in course)
