# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)
    a = 5

    # TODO: What was the warmest day in the data set?
    warmest_dict = {}
    highest_temp = -1000
    for w in weatherdata:
        if w['tmax'] > highest_temp:
            highest_temp = w['tmax']
            warmest_dict = w

    print("warmest day was ", warmest_dict['date'])

    warmest = max(weatherdata, key=lambda x: x['tmax'])
    print("warmest day was ", warmest['date'])

# TODO: What was the coldest day in the data set?
    coldest = min(weatherdata, key=lambda x: x['tmin'])
    print("cooldest day was ", coldest['date'])

# TODO: How many days had snowfall?
snowdays = [day for day in weatherdata if day['snow']>0]
print(len(snowdays))