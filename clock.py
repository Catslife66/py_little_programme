import datetime


class Clock:
    def __init__(self, ringtone, snooze_time):
        self.now = datetime.datetime.now()
        self.ringtone = ringtone
        self.ringing = False
        self.awake = False
        self.snooze_time = snooze_time

    def show_time(self):
        return datetime.datetime.strftime(self.now, '%H:%M')

    def set_alarm(self, h, m, s):
        if h == self.now.hour and m == self.now.minute and s == self.now.second:
            self.ring()

    def ring(self):
        self.ringing = True

    def wake(self):
        self.awake = True
        self.ringing = False

    def snooze(self):
        self.awake = False
