"""
ID: s.sophi1
LANG: PYTHON2
PROG: friday
"""

input = open('friday.in', 'r')
output = open('friday.out', 'w')
number_of_years = int(input.readlines()[0])
input.close()


def find_leap_years(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def find_thirteenths(first_day_week, month_len):
    thirteenth_day = (first_day_week+12) % 7
    last_day = (first_day_week + month_len-1) % 7
    return thirteenth_day, last_day


def month_length(month, year):
    if month == 9 or month == 11 or month == 4 or month == 6:
        return 30
    elif month != 2:
        return 31
    else:
        if find_leap_years(year) == False:
            return 28
        else:
            return 29


week_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    0: 0,
}

year = 1900
last_day = 0

for year in range(1900, 1900 + number_of_years):
    for month in range(1, 13):
        length = month_length(month, year)
        thirteenth_day, last_day = find_thirteenths((last_day+1)%7, length)
        print year, month, thirteenth_day
        week_count[thirteenth_day] += 1

answer_list = [week_count[6], week_count[0], week_count[1], week_count[2], week_count[3], week_count[4], week_count[5]]
output.write(' '.join([str(answer) for answer in answer_list]) + '\n')
output.close()
