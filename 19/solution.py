def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_in_month(month, year):
    if month in (3, 5, 8, 10):
        return 30
    if month == 1:
        if is_leap_year(year):
            return 29
        return 28
    return 31

def main():
    min_year = 1901
    max_year = 2001
    count = 0
    year = 1900
    month = 0
    day = 1
    date = 0
    while year < max_year:
        month = month % 12
        dates = days_in_month(month, year)
        for date in range(dates):
            if year >= min_year and day == 0 and date == 0:
                count += 1
            day = (day + 1) % 7
        month = (month + 1) % 12
        if month == 0:
            year += 1
    print(count)

if __name__ == '__main__':
    main()
