class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print(f"You can Drive {self.model}")

    def stop(self):
        print(f"You can Stop {self.model}")