class Car:
    runs = True

    def start(self, name):
        self.name = name

        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken :( !")

Car.runs = False
volvo = Car()

volvo.start("volvo")