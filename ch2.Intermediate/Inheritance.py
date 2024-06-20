class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Cat(Animal):
    def sound(self):
        print("MEOW!")

class Dog(Animal):
    def sound(self):
        print("WOOF!")

class Bird(Animal):
    def sound(self):
        print("TWEET!")

cat = Cat("Bobo")
dog = Dog("Mike")
bird = Bird("Blue")

print(cat.name)
cat.eat()
cat.sleep()
