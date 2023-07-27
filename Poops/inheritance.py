class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def get_vehicle(self):
        print("This car is a ", self.name, self.model, end="")


class FuelCar(Vehicle):
    def __init__(self, name, model, combust_tpe):
        self.combust_type = combust_tpe
        Vehicle.__init__(self, name, model)

    def get_fuel_car(self):
        super().get_vehicle()
        print(", combust type is", self.combust_type, end="")


class ElectricCar(Vehicle):
    def __init__(self, name, model, battery_power):
        Vehicle.__init__(self, name, model)
        self.battery_power = battery_power

    def get_electric_car(self):
        super().get_vehicle()
        print(", battery power is ", self.battery_power, end="")


class GasolineCar(FuelCar):
    def __init__(self, name, model, combust_type, gas_capacity):
        FuelCar.__init__(self, name, model, combust_type)
        self.gas_capacity = gas_capacity

    def get_gasoline_car(self):
        super().get_fuel_car()
        print(", gas capacity is ", self.gas_capacity, end="")


class HybridCar(ElectricCar, GasolineCar):
    def __init__(self, name, model, battery_power, combust_type, gas_capacity):
        ElectricCar.__init__(self, name, model, battery_power)
        GasolineCar.__init__(self, name, model, combust_type, gas_capacity)
        self.battery_power = battery_power

    def get_hybrid_car(self):
        self.get_fuel_car()
        print(", battery power is ", self.battery_power)


print("Single Inheritance: ")
Fuel = FuelCar("Honda", "Accord", "Petrol")
Fuel.get_fuel_car()
print("-"*20)

print("Hierarchical Inheritance: ")
Electric = ElectricCar("Tesla", "model S", "200MWH")
Electric.get_electric_car()
print("*"*20)

print("Multilevel Inheritance: ")
Gasoline = GasolineCar("Toyota", "Corolla", "gasoline", "16L")
Gasoline.get_gasoline_car()
print("^"*20)

print("Multiple Inheritance: ")
Hybrid = HybridCar("Tata", "Nexon", "300MWH", "Petrol", "30L")
Hybrid.get_hybrid_car()










