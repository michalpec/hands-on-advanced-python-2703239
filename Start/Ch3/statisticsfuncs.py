# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
max_temps = [d['tmax'] for d in summer_months]
min_temps = [d['tmin'] for d in summer_months]

avg_max_temp = statistics.mean(max_temps)
avg_min_temp = statistics.mean(min_temps)
print(avg_max_temp)
print(avg_min_temp)

# TODO: calculate the median values for min and max temperatures

median_max_temp = statistics.median(max_temps)
median_min_temp = statistics.median(min_temps)
print(median_max_temp)
print(median_min_temp)
# TODO: use the standard deviation function to find outlier temperatures

upper_outlier = avg_max_temp + statistics.stdev(max_temps) *2
lower_outlier = avg_min_temp - statistics.stdev(min_temps) *2

print(upper_outlier, lower_outlier)

max_outliers = list(filter(lambda d : d['tmax'] >= upper_outlier, summer_months))
min_outliers = list(filter(lambda d : d['tmin'] <= lower_outlier, summer_months))

print(max_outliers)
print(min_outliers)