# We use classes to define new types to model real concepts

# Use Pascal naming convention
# No fields! Use attributes instead
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10  # Attributes (like setting fields outside of constructor)
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
