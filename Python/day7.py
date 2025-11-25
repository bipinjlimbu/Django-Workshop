#inheritance
class vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}\nModel: {self.model}")

class car(vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

c1 = car("Toyota", "Corolla", "Red")
c1.display_info()