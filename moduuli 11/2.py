
class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.mileage = 0
#----------------------------------------------------------------------
    def set_speed(self, speed):
        self.current_speed = min(speed, self.top_speed)
#----------------------------------------------------------------------
    def drive(self, hours):
        self.mileage += self.current_speed * hours
#----------------------------------------------------------------------


class ElectricCar(Car):
    def __init__(self, registration_number, top_speed, battery_capacity):
        super().__init__(registration_number, top_speed)
        self.battery_capacity = battery_capacity  
#----------------------------------------------------------------------


class CombustionEngineCar(Car):
    def __init__(self, registration_number, top_speed, gas_tank_size):
        super().__init__(registration_number, top_speed)
        self.gas_tank_size = gas_tank_size  
#----------------------------------------------------------------------

electric_car = ElectricCar("ABC-15", 180, 52.5)
combustion_car = CombustionEngineCar("ACD-123", 165, 32.3)


electric_car.set_speed(150) 
combustion_car.set_speed(120) 


electric_car.drive(3)
combustion_car.drive(3)


print(f"Electric Car {electric_car.registration_number} has driven {electric_car.mileage} km.")
print(f"Combustion Engine Car {combustion_car.registration_number} has driven {combustion_car.mileage} km.")
