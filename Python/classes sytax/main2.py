class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(240, 18)
modelY = Vehicle(210, 13)
modelZ = Vehicle(300, 10)

print("\nModel X\n")
print("Model max speed: ", modelX.max_speed)
print("Model mileage: ", modelX.mileage)

print("\nModel Y\n")
print("Model max speed: ", modelY.max_speed)
print("Model mileage: ", modelY.mileage)

print("\nModel Z\n")
print("Model max speed: ", modelZ.max_speed)
print("Model mileage: ", modelZ.mileage)