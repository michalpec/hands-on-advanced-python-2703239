# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function

import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?

total_snowfall = reduce(lambda acc, d : acc + d['snow'], weatherdata, 0)
print(total_snowfall)
# TODO: how much total precipitation is in the entire dataset?

total_precip = reduce(lambda acc, d : acc + d['snow'] + d['prcp'], weatherdata, 0)
print(total_precip)
# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
def warm_snow_day(acc, elem):
    return elem if elem['snow']>0 and elem['tmax'] > acc['tmax'] else acc
    # return the elem value if the snow amount > 0 and its tmax value is
    # larger than the tmax value that is in the acc argument
    pass

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}

# TODO: reduce the data set to the warmest snow day
wsd = reduce(warm_snow_day, weatherdata, start_val)
print(wsd)


snowfall_days = filter(lambda d : d['snow']>0, weatherdata)
maxtem_snowfall_day = max(snowfall_days, key=lambda d: d['tmax'])
print(maxtem_snowfall_day)