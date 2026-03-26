import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        # Keep speed within limits
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours



# TASK 1,2,3

car = Car("ABC-123", 142)

print("Initial car info:")
print(car.registration_number, car.max_speed, car.current_speed, car.travelled_distance)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("\nSpeed after acceleration:", car.current_speed)

car.accelerate(-200)
print("Speed after emergency brake:", car.current_speed)

car.current_speed = 60
car.travelled_distance = 2000
car.drive(1.5)
print("Distance after driving:", car.travelled_distance)


# TASK 4: CAR RACE

cars = []

# Create 10 cars
for i in range(10):
    reg = f"ABC-{i+1}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

race = True

while race:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race = False

print("\n--- RACE RESULTS ---")
print(f"{'Reg':<10} {'Max':<10} {'Speed':<10} {'Distance':<15}")

for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<15.2f}")