for item in 'Python':
    print(item)

print()

# for item in ["Eric", "John", "Sarah"]:
#     print(item)

# for item in [1, 2, 3, 4, 5]:
#      print(item)

for item in range(10):  # range function, [0, 9]
    print(item)

print()

for item in range(5, 10):
    print(item)

print()

for item in range(5, 9, 2):  # optionally takes a step
    print(item)

print()

prices = [10, 20, 30]
total_price = 0
for price in prices:
    total_price += price
print(f"Total: {total_price}")
