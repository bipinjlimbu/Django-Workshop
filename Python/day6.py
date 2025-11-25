class car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Car Brand: {self.brand}, Color: {self.color}")

c1 = car("Toyota", "Red")
c1.display_info()