import random


class Car:
    def __init__(car, registration_number, top_speed):
        car.registration_number = registration_number
        car.top_speed = top_speed
        car.current_speed = 0
        car.distance_traveled = 0


    def accelerate(car, speed_change):
        new_speed = car.current_speed + speed_change
        if new_speed > car.top_speed:
            car.current_speed = car.top_speed
        elif new_speed < 0:
            car.current_speed = 0
        else:
            car.current_speed = new_speed

    def go(car, hours):
        car.distance_traveled += car.current_speed * hours

#------------------------------------------------------------------------
cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]


race_finished = False
while not race_finished:
    for car in cars:

        car.accelerate(random.randint(-10, 15))

        car.go(1)


        if car.distance_traveled >= 10000:
            race_finished = True
            break


print(f"{'Registration':<12} {'Top Speed':<10} {'Current Speed':<14} {'Distance Traveled':<18}")
print("=" * 54)
for car in cars:
    print(f"{car.registration_number:<12} {car.top_speed:<10} {car.current_speed:<14} {car.distance_traveled:<18}")
