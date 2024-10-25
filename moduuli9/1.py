class Car:
    def __init__(car, registration_number, top_speed):
        car.registration_number = registration_number
        car.top_speed = top_speed
        car.current_speed = 0
        car.distance_traveled = 0

my_car = Car("ABC-123",142)

print(my_car.registration_number , my_car.top_speed ,my_car.current_speed , my_car.distance_traveled) 