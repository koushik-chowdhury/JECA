class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + " @"
    def full_name(self):    # adding functionality
        return f"{self.__brand} {self.model}"
    

my_Car = Car("Mahindra", "Scorpio")

print(my_Car.get_brand())
print(my_Car.model)
print(my_Car.full_name())