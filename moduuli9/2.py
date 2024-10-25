class Car:
    def __init__(car, top_speed):
        if 0 < top_speed <= 147:
            car.top_speed = top_speed  
            car.current_speed = 0 
        else:
            ("The Top Speed must be equal or less than 147 km/h")  

    def accelerate(car, speed_change):
        new_speed = car.current_speed + speed_change
        
        if new_speed > car.top_speed:
            car.current_speed = car.top_speed
        elif new_speed < 0:
            car.current_speed = 0
            print("The car's speed cannot decrease below (0 km/h)")
        else:
            car.current_speed = new_speed

        print(f"Current Speed: {car.current_speed} km/h") 

# البرنامج الرئيسي
mycar = Car(147)
mycar.accelerate(30) 
mycar.accelerate(70) 
mycar.accelerate(50) 
mycar.accelerate(-200)
