# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it

import json
import pandas as pd
import pprint


def __load_data(path):
    with open(path, 'r') as datafile:
        dat = json.load(datafile)
        return dat


def load_data():
    return __load_data(r'../../sample-weather-history.json')


def count_days_in_year(data:{}) ->{}:
    years = {}

    for d in data:
        date = d['date']
        year = date.split('-')[0]
        if year in years.keys():
            years[year] +=1
        else:
            years[year] = 1

    return years

# TODO: open the sample weather data file and use the json module to load and parse it
data = load_data()

# TODO: make sure the data loaded correctly by printing the length of the dataset
print(len(data))
# TODO: let's also take a look at the first item in the data
pprint.pp(data[0])

# TODO: How many days of data do we have for each year?

pprint.pp(count_days_in_year(data))
# if __name__ == "__main__":
#     data = load_data()
#     print(data)
