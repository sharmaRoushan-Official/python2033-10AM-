class Car:
    def start(self):
        print("Car starts with a key")

class Bike:
    def start(self):
        print("Bike starts with a kick")
# c = Car()
# c.start()


def start_vehicle(vehicle):
    vehicle.start()

start_vehicle(Car())
start_vehicle(Bike())