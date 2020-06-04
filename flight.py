class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


LHR_JFK = Flight(275)

people = ["Harry", "Ron", "Hermione", "Ginny", "Draco"]

for person in people:
    if LHR_JFK.add_passenger(person):
        print(f"Successfully added {person} to flight")
    else:
        print(f"Not enough seats")
