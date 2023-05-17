import datetime


class Flight:
    def __init__(self, model, capacity, price):
        self.model = model
        self.capacity = capacity
        self.price = price
        self.passengers = []
        self.over_booking = False

    def booking(self, name):
        if not self.over_booking:
            self.passengers.append(name)
        if len(self.passengers) >= self.capacity:
            self.over_booking = True

    def calculate_selling(self):
        return self.price * len(self.passengers)


class User:
    def __init__(self, name, gender, age, nationality, id_no, ac_no):
        self.name = name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.id_no = id_no
        self.ac_no = ac_no
        self.new_booking = []
        self.history_booking = []

    def on_booking(self, flight, price, takeoff):
        booking_info = {'flight': flight, 'price': price, 'takeoff': takeoff}
        self.new_booking.append(booking_info)

    def history_journey(self):
        t = datetime.datetime.now()
        for booking in self.new_booking:
            if booking['takeoff'] == f'{t.date()}, {t.hour}:{t.minute}':
                self.new_booking.remove(booking)
                self.history_booking.append(booking)


f = Flight('boeing 747', 3, 100)
f.booking('John')
f.booking('Kate')
f.booking('Liz')
f.booking('Tom')
f.booking('Lily')


u = User('Tom', 'M', 32, 'British', 123456, 123456)
u.on_booking('CZ303', 500, '2022-09-06, 9:30')
u.on_booking('CZ333', 700, '2022-09-06, 9:35')
u.on_booking('CZ333', 700, '2022-09-06, 9:39')
u.history_journey()
print(u.new_booking)
