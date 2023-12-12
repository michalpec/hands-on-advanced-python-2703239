# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snowydays_it = filter(lambda d:d['snow'] > 0, weatherdata)
snowydays = list(snowydays_it)
print(snowydays)
# TODO: pretty-print the resulting data set
pprint.pp(snowydays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_months = [7, 8]
    month = d['date'].split('-')[1]
    res = int(month) in summer_months and d['prcp'] >=1
    # if res:
    #     a=5
    return res

rainysummerdays = list(filter(is_summer_rain_day, weatherdata))
print(len(rainysummerdays))
# pprint.pp(rainysummerdays)