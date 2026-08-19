class Car:
    def __init__(self, brand, model):
        self.__brand = brand            ## making __variable == private
        self.model = model
    def full_name(self):
        return f'{self.__brand} {self.model}'
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):                  # Polymorphism
        return "Diesel or petrol"

    @staticmethod       # Cannot be accessible by objects of this class 
    def car_description():
        return "This Class if of Cars and This is written in Static method" 
        



class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize  
    def fuel_type(self):                             # Polymorphism
        return "Electric"

car1 = Car("BMW","i8")

# print(car1.model)
# print(car1.full_name())

my_tesla = ElectricCar("Tesla","Model S","8KWh")

# print(my_tesla.full_name())
# print(my_tesla.batterySize)
# print(car1.get_brand())

print(car1.fuel_type())
print(my_tesla.fuel_type())

print(Car.car_description())