from parsedata import load_data





def cold_windy_rainy(d):

    rainy_or_snowy = (d['prcp'] + d['snow']) > 0.7
    windy = d['awnd'] > 10.0 if d['awnd'] else False
    cold = d['tmin'] < 45

    return windy and cold and rainy_or_snowy

def get_cold_windy_rainy_days():
    weatherdata = load_data()
    return list(filter(cold_windy_rainy, weatherdata))

print(get_cold_windy_rainy_days())