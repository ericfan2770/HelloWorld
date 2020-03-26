import random  # built-in module

for i in range(3):
    #  print(random.random())
    print(random.randint(10, 20))  # inclusive for start and end

print()

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)

print()

# Exercise


class Dice:
    def roll(self):
        num_1 = random.randint(1, 6)
        num_2 = random.randint(1, 6)
        result = num_1, num_2  # automatically a tuple without line breaks
        return result


dice_1 = Dice()
print(dice_1.roll())


