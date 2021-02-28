class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set_time(self, hours, minutes, seconds):
        self.seconds = seconds
        self.hours = hours
        self.minutes = minutes

    def get_time(self):
        time = ""
        if self.hours <= 9:
            time += f"0{self.hours}:"

        else:
            time += f"{self.hours}:"

        if self.minutes <= 9:
            time += f"0{self.minutes}:"

        else:
            time += f"{self.minutes}:"

        if self.seconds <= 9:
            time += f"0{self.seconds}"

        else:
            time += f"{self.seconds}"

        return time

    def next_second(self):
        self.seconds += 1

        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1

        if self.hours > Time.max_hours:
            self.hours = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time1 = Time(10, 59, 59)
print(time1.next_second())

time2 = Time(23, 59, 59)
print(time2.next_second())
