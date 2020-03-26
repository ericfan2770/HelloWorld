course = 'Python for Beginners'
# print(course)

course = "Python's Course for Beginners"
# print(course)

course = 'Python for "Beginners"'
# print(course)

course = '''Python's Course for "Beginners"'''
# print(course)

course = '''
Printing in multiple
lines!
'''

course = "Python for Beginners"
         #0123456789
# This is like the Java charAt method
print(course[0])    # Zero-indexed
print(course[3])
print(course[-2])   # second character from the end

# This is like Java substring method
print(course[0:3])  # Still [inclusive:exclusive]
print(course[3:])   # Like substring(3)
print(course[:5])   # From beginning to last index, exclusive
print(course[:])    # Empty means 0 for left, len for right

# Exercise
name = 'Jennifer'
print(name[1:-1])   # prints 'ennife'
