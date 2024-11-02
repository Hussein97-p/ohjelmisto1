class Elevator:
    def __init__(self, lowest=1, highest=5):
        self.lowest = lowest
        self.highest = highest
        self.current = lowest

    def move_to(self, target):
        if target < self.lowest or target > self.highest:
            print("Invalid input")
            return
        while self.current != target:
            self.current += 1 if self.current < target else -1
            print(f"The elevator is now on floor {self.current}.")
        print(f"Arrived at floor {self.current}.")

    def return_to_lowest(self):
        self.move_to(self.lowest)


class House:
    def __init__(self, lowest=1, highest=5, num_elevators=1):
        self.elevators = [Elevator(lowest, highest) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {target}.")
            self.elevators[elevator_number - 1].move_to(target)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        print("Fire alarm! All elevators going to ground floor.")
        for elevator in self.elevators:
            elevator.return_to_lowest()



house = House(lowest=1, highest=5, num_elevators=2)


house.run_elevator(1, 4)
house.run_elevator(2, 3)


house.fire_alarm()
