class ConcertHall:
    def __init__(self, name, total_seats, booked_seats=0):
        self._name = name
        self.total_seats = total_seats
        self.booked_seats = booked_seats
    @property
    def name(self):
        return self._name
    @property
    def total_seats(self):
        return self._total_seats
    @total_seats.setter
    def total_seats(self, value):
        if value < 1:
            raise ValueError("Total seatss must be at least 1")
        self._total_seats = value
    @property
    def booked_seats(self):
        return self._booked_seats
    @booked_seats.setter
    def booked_seats(self, value): 
        if value < 0:
            raise ValueError("Booked seats cannot be negative")
        elif value > self.total_seats:
            raise ValueError("Bookes seats cannot exceed total seats")
        self._booked_seats = value
    @property
    def available_seats(self):
        return self.total_seats - self.booked_seats
    @property
    def booking_rate(self):
        return round((self.booked_seats / self.total_seats) * 100, 1)
    def reserve(self, seats):
        if seats < 0:
            raise ValueError("Number of seats must be positive")
        elif self.booked_seats + seats > self.total_seats:
            raise ValueError("Not enough empty seats")
        else:
            self.booked_seats += seats
    def cancel(self, seats):
        if seats < 0:    
            raise ValueError("Number of seats must be positive")
        elif self.booked_seats - seats < 0:
            raise ValueError("Cannot cancel more than booked")
        else:
            self.booked_seats-= seats

h = ConcertHall("Grand", 200)
print(h.name, h.available_seats, h.booking_rate)

h.reserve(150)
print(h.booked_seats, h.booking_rate)

h.cancel(30)
print(h.available_seats)

try:
    h.reserve(100)
except ValueError as e:
    print(e)

try:
    h.name = "X"
except AttributeError:
    print("Cannot change hall name")
