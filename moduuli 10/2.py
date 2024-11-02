class Elevator:
    def __init__(self, lowest_floor_number=1, highest_floor_number=5):
        self.lowest_floor_number = lowest_floor_number
        self.highest_floor_number = highest_floor_number
        self.current_floor = lowest_floor_number
#----------------------------------------------------------------------------------------------------------
    def move_to_floor(self, target_floor):
        if not self.is_valid_floor(target_floor):
            print("Invalid input")
            return
        while self.current_floor != target_floor:
            self.move_elevator(target_floor)
        print(f"You have arrived at floor {self.current_floor}.")
#----------------------------------------------------------------------------------------------------------
    def is_valid_floor(self, floor):
        return self.lowest_floor_number <= floor <= self.highest_floor_number
#----------------------------------------------------------------------------------------------------------
    def move_elevator(self, target):
        if self.current_floor < target:
            self.floor_up()
        elif self.current_floor > target:
            self.floor_down()
#----------------------------------------------------------------------------------------------------------
    def floor_up(self):
        if self.current_floor < self.highest_floor_number:
            self.current_floor += 1
            print(f"The elevator is now on floor {self.current_floor}.")
        else:
            print("You are already at the highest floor")
#----------------------------------------------------------------------------------------------------------
    def floor_down(self):
        if self.current_floor > self.lowest_floor_number:
            self.current_floor -= 1
            print(f"The elevator is now on floor {self.current_floor}.")
        else:
            print("You are already at the lowest floor")

    def return_to_lowest_floor(self):
        self.move_to_floor(self.lowest_floor_number)

#----------------------------------------------------------------------------------------------------------
class House:
    def __init__(self, lowest_floor_number=1, highest_floor_number=5, number_of_elevators=1):
        self.elevators = [Elevator(lowest_floor_number, highest_floor_number) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {target_floor}.")
            self.elevators[elevator_number - 1].move_to_floor(target_floor)
        else:
            print("Invalid elevator number")

#----------------------------------------------------------------------------------------------------------

house = House(lowest_floor_number=1, highest_floor_number=5, number_of_elevators=2)


house.run_elevator(1, 4)


house.elevators[0].return_to_lowest_floor()


house.run_elevator(2, 3)


house.elevators[1].return_to_lowest_floor()
