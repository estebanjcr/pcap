# Class Timer

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if hours in range(0, 24):
            self.__hrs = hours
        else:
            raise ValueError
        if minutes in range(0, 60):
            self.__mins = minutes
        else:
            raise ValueError
        if seconds in range(0, 60):
            self.__secs = seconds
        else:
            raise ValueError

    def __str__(self):
        
        if self.__hrs < 10:
            hh = "0" + str(self.__hrs)
        else:
            hh = str(self.__hrs)
        
        if self.__mins < 10:
            mm = "0" + str(self.__mins)
        
        else:
            mm = str(self.__mins)
        
        if self.__secs < 10:
            ss = "0" + str(self.__secs)
        else:
            ss = str(self.__secs)
        
        time = hh + ":" + mm + ":" + ss
        
        return time

    def next_second(self):
        if self.__secs < 59:
            self.__secs += 1
        else:
            self.__mins += 1
            self.__secs = 0
            if self.__mins == 60:
                self.__hrs += 1
                self.__mins = 0
                if self.__hrs == 24:
                    self.__hrs = 0

    def prev_second(self):
        if self.__secs > 0:
            self.__secs -= 1
        else:
            self.__secs = 59
            if self.__mins > 0:
                self.__mins -= 1
            else:
                self.__mins = 59
                if self.__hrs > 0:
                    self.__hrs -= 1
                else:
                    self.__hrs = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)