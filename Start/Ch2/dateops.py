# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
from datetime import date, timedelta

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily


# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)


# TODO: what was the warmest weekend day in the dataset?

def is_weekend_from_datestring(datestr: str) -> bool:
    dt = date.fromisoformat(datestr)
    wd = dt.weekday()
    return wd in([5, 6])

def is_weekend(d) -> bool:
    return is_weekend_from_datestring(d['date'])


weekenddays = list(filter(is_weekend, weatherdata))

warmest_weekend_day = max(weekenddays, key = lambda d : d['tmax'])
print(warmest_weekend_day)
# dts = "2023-12-08"
# print(is_weekend(dts))
# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days

avg_acc = 0
next_day = coldest_date

for nd in range(7):
    next_day += timedelta(days = 1)
    data = next((day for day in weatherdata if day['date'] == str(next_day)), None)
    avg_acc += (data['tmin'] + data['tmax'])/2

avg_temp = avg_acc / 7

print(avg_temp)