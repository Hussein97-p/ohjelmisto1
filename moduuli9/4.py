import random


class Car:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0


    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def go(self, hours):
        self.distance_traveled += self.current_speed * hours

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
