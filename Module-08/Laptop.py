class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age
    def increase_age(self , age = 1):
        self.last_age = self.age
        self.age = self.age + age

    def repair(self, life_increase = -5):
        self.life_increase = life_increase

my_laptop = Laptop('Acer', 2)
my_laptop.increase_age()
my_laptop.increase_age()
my_laptop.age = 16
my_laptop.increase_age()
print(my_laptop.age)
my_laptop.repair(-7)
print(my_laptop.age)