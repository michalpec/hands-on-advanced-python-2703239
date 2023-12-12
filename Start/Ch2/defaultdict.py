# Example file for Advanced Python: Hands On by Joe Marini
# Count items using a default dictionary

import json
import pprint
from collections import defaultdict


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


def count_days_in_year(data:{}) ->{}:
    years = defaultdict(int)

    for d in data:
        date = d['date']
        year = date.split('-')[0]
        years[year] +=1

    return years






# The defaultdict collection provides a cleaner way of initializing key values
# TODO: Count the number of data points for each year we have data
pprint.pp(count_days_in_year(weatherdata))

# TODO: defaultdict can use more complex objects, like lists
def count_days_in_year_month(data: {}) -> {}:
    years_months = defaultdict(list)

    for d in data:
        date = d['date']
        spl = date.split('-')
        year = spl[0]
        month = spl[1]
        key = '-'.join([year, month])


        years_months[key].append(d)

    return years_months

years_months_dict = count_days_in_year_month(weatherdata)

print(len(years_months_dict))



# TODO: create a dictionary with year-month keys and lists for each day in the month


# What were the coldest and warmest days of each month?
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])

for year_month, daydata in years_months_dict.items():
    print("warmest day: ", warmest_day(daydata))
    print("coldest day: ", coldest_day(daydata))

# TODO: loop over the keys of the dictionary and find each warmest and coldest day
