class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production  # litr/kun

    def produce_milk(self):
        print(f"{self.name} produces {self.milk_production} liters of milk per day.")

class Chicken(Animal):
    def __init__(self, name, age, egg_production):
        super().__init__(name, age)
        self.egg_production = egg_production  # dona/kun

    def lay_eggs(self):
        print(f"{self.name} lays {self.egg_production} eggs per day.")

class Pig(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight  # kg

    def oink(self):
        print(f"{self.name} says: Oink!")

# Misol ishlatish
cow1 = Cow("Bessie", 4, 10)
cow1.eat()
cow1.produce_milk()

chicken1 = Chicken("Clucky", 2, 5)
chicken1.lay_eggs()

pig1 = Pig("Porky", 3, 150)
pig1.oink()
pig1.sleep()
