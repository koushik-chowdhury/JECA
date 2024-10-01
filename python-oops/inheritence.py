class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):    # adding functionality
        return f"{self.brand} {self.model} {self.additional_details()}"
    def additional_details(self):
        return ""

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def additional_details(self):
        return self.battery_size



my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.full_name())

my_Car = Car("Mahindra", "Scorpio")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())


tata_car = Car("Tata", "Nano")
print(tata_car.brand)
print(tata_car.model)
print(tata_car.full_name())