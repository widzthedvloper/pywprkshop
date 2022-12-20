class Car:
    runs = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"{self.name} --> {Car.runs}"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :( !")

Car.runs = False
volvo = Car("Volovo")

volvo.start()

print(volvo)
print(repr(volvo))