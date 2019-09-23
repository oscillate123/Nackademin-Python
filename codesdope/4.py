"""
Create a Time class and initialize it with hours and minutes.

1. Make a method addTime which should take two time object and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)

2. Make a method displayTime which should print the time.

3. Make a method DisplayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.
"""
from datetime import datetime


class Time:
    def __init__(self, hr1, min1, hr2, min2):
        self.hr1 = hr1
        self.min1 = min1
        self.hr2 = hr2
        self.min2 = min2

    def add_time(self):
        tot_hours = self.hr1 + self.hr2
        tot_min = self.min1 + self.min2

        if tot_min > 59:
            tot_hours += tot_min//60
            tot_min = tot_min % 60

        return tot_hours, tot_min

    def display_time(self):
        x = datetime.now().hour
        y = datetime.now().minute
        return f"{x}:{y}"

    def display_minute(self):
        x = datetime.now().hour
        y = datetime.now().minute
        tot_minute = 0
        tot_minute += y

        if x > 0:
            tot_minute += (x*60)

        return tot_minute


x = Time(1, 40, 2, 50)
print(x.add_time())
print(x.display_time())
print(x.display_minute())
