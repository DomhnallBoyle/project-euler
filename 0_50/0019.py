# counting sundays

def is_century(year):
    return str(year)[-2:] == '00'


def is_leap_year(year):
    if year % 4 != 0:
        return False
    
    if is_century(year):
        if year % 400 == 0:
            return True
        return False

    return True


def main():
    months = [
        'sept',
        'oct',
        'nov',
        'dec',
        'jan',
        'feb',
        'mar',
        'apr',
        'may',
        'june',
        'july',
        'aug'
    ]
    month_to_next_month_d = {months[i]: months[i + 1] for i in range(len(months) - 1)}
    month_to_next_month_d['aug'] = 'sept'
    months_to_days_d = {
        'sept': 30,
        'oct': 31,
        'nov': 30,
        'dec': 31,
        'jan': 31,
        'feb': 28,
        'mar': 31,
        'apr': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'aug': 31
    }
    day, month, year = 1, 'jan', 1901  # we know this is Tuesday if 01/01/1900 was a Monday
    day += 5  # this is the first sunday
    days_per_week = 7
    days_per_month = months_to_days_d[month]
    sunday_count = 1

    while (month, year) != ('jan', 2001):

        # iterate over the sundays
        while day < days_per_month:
            day += days_per_week

        # new month + year potentially
        month = month_to_next_month_d[month]
        if month == 'jan':
            year += 1

        # reset the days
        day = (day - days_per_month) + 1  # if day == 0, we need to +1
        if day == 1:
            sunday_count += 1

        # reset the days per month
        days_per_month = months_to_days_d[month]
        if month == 'feb' and is_leap_year(year):
            days_per_month += 1

    print(sunday_count)
    print(day, month, year)


if __name__ == '__main__':
    main()
