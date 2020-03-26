# We use classes to define new types to model real concepts

# Use Pascal naming convention
# No fields! Use attributes instead
class Point:
    def __init__(self, x , y):  # constructor: short for initialize, self is like "this" keyword in Java
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)

# Exercise
class Person:
    def __init__(self, name):  # self should always be the very first parameter
        self.name = name

    def talk(self):
        print(f"Hi! I am {self.name}!")


person = Person("Eric")
person.talk()

person = Person("Bob")
person.talk()
