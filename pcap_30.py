# the calendar module

import calendar

class Calendar():
    pass

class MyCalendar(Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year=2000, weekday=0):
        try:
            if year not in range(1, 2025):
                raise ValueError
            if weekday not in range(0, 7):
                raise ValueError
        except ValueError:
        	print('Invalid input.')
        	return
        	
        c = calendar.Calendar()
        count = 0
        for month in range(1, 13):
            for week in c.monthdays2calendar(year, month):
        	    for day in week:
        	        if day[0] != 0 and day[1] == weekday:
        		        count += 1
        print(count)

cal = MyCalendar()
cal.count_weekday_in_year(year=2019, weekday=0)
