class ParkingSystem:
    def __init__(self, big, medium, small):
        self.slots = [big, medium, small]

    def addCar(self, carType):
        self.slots[carType - 1] -= 1
        return self.slots[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
