"""
Create a Time class and initialize it with hours and minutes.

1. Make a method addTime which should take two time object and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)

2. Make a method displayTime which should print the time.

3. Make a method DisplayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.
"""


class Time:
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    @staticmethod
    def add_time(time1, time2):
        tot_hours = time1.hr + time2.hr
        tot_min = time1.min + time2.min

        if tot_min > 59:
            tot_hours += tot_min // 60
            tot_min = tot_min % 60

        return f"{tot_hours}h {tot_min}min"

    def display_time(self):
        return f"The time is: {self.hr}:{self.min}"

    def display_minute(self):
        hr2min = self.hr*60
        tot_min = hr2min+self.min
        return tot_min


x = Time(1, 50)
y = Time(2, 10)
z = Time(0, 0)
print(x.hr, x.min)
a = Time.add_time(x, y)
print(a)
print(x.display_time())
print(x.display_minute())
