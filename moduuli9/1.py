class Car:
    def __init__(self,registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

my_self = Car("ABC-123",300)