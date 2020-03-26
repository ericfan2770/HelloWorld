coordinates = (1, 2, 3)  # (x, y, z)
#  coordinates[0] * coordinates[1] * coordinates[2]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x * y * z)
print()

# Unpacking -- performs same action as lines 3-5, and much shorter and concise!
# Works with lists and tuples
x, y, z = coordinates
print(x)
print(y)
print(z)