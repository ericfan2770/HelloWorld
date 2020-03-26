# Inheritance: mechanism to reuse code
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # Dog inherits from Mammal
    # pass -- if Dog has no unique methods
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()
