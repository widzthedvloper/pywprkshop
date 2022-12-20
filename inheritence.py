class Car: 
    def start(self):
        print("Started!!")

class Truck:
    def load(self):
        print("Loaded!!")


class TopDrop(Car, Truck):
    pass

my_top_drop = TopDrop()

my_top_drop.start()
my_top_drop.load()