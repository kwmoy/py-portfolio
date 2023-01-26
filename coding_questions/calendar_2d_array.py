# Prompt: Create a 2D array representing a calendar month given:
# (1) the day of week (0-6) that the month begins, and
# (2) the number of days in the month

# Desired output: A Sun - Sat calendar. For example,
# Input for Dec 2021 would be:
# (4, 31)

# Output for Dec 2021 would be:
# [[ 0,  0,  0,  0,  1,  2,  3],
#  [ 4,  5,  6,  7,  8,  9, 10],
#  [11, 12, 13, 14, 15, 16, 17],
#  [18, 19, 20, 21, 22, 23, 24],
#  [25, 26, 27, 28, 29, 30, 31]]

def create_calendar_month_array(day_of_week_start: int, days_in_month: int):
    if day_of_week_start < 0 or day_of_week_start > 6:
        raise Exception("Day of week input is not valid!")

    month_array = []
    week_array = [0]*day_of_week_start

    for i in range(0, days_in_month):
        week_array.append(i+1)

        while i == days_in_month - 1 and len(week_array) < 7:
            week_array.append(0)
        if len(week_array) == 7:
            month_array.append(week_array)
            week_array = []
    return month_array


print(create_calendar_month_array(3, 28))

