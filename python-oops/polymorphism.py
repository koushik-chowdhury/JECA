class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):    # adding functionality
        return f"{self.brand} {self.model}"

my_Car = Car("Mahindra", "Scorpio")

print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())


