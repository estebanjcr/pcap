def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(year) == True and month == 2:
        return 29
    elif is_year_leap(year) == False and month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return None

def day_of_year(year, month, day):
    total_days = 0
    for m in range(month):
        total_days += days_in_month(year, m + 1)
    return total_days

print(day_of_year(2000, 3, 31))
