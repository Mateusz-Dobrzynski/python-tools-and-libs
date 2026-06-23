from datetime import date

TODAY=date(2026, 1, 14)

def is_loyal(customer):
    return days_between(customer["join_date"], TODAY) >= 1000


def days_between(start: date, end: date) -> int:
    if start > end:
        temp = end
        end = start
        start = temp
    if start.month == end.month and start.year == end.year:
        return end.day - start.day
    if start.year == end.year:
        return dates_in_the_same_year(start, end)
    else:
        return dates_in_different_years(start, end)


def dates_in_the_same_year(start: date, end: date):
    days = number_of_days_in_month(start.month, start.year) - start.day
    for month in range(start.month + 1, end.month):
        days += number_of_days_in_month(month, start.year)
    return days + end.day


def dates_in_different_years(start: date, end: date):
    days = number_of_days_in_month(start.month, start.year) - start.day
    for month in range(start.month + 1, 13):
        days += number_of_days_in_month(month, start.year)
    for year in range(start.year + 1, end.year):
        days += 366 if is_leap_year(year) else 365
    for month in range(1, end.month):
        days += number_of_days_in_month(month, end.year)
    return days + end.day


def number_of_days_in_month(month: int, year):
    if month in (8, 12):
        return 31
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    elif month % 2 == 0:
        return 30
    else:
        return 31


def is_leap_year(year: int):
    if year % 4 == 0:
        return True
    if year % 400 == 0:
        return True
    return False
