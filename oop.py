class Car:
    runs = True

    def __init__(self, name):
        self.name = name

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :( !")

Car.runs = False
volvo = Car("Volovo")

volvo.start()