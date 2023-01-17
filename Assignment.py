import json
with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# Part 1, 2
dict_seattle= []
for measurement in precipitation:
    station_code = measurement['station']
    if station_code == 'GHCND:US1WAKG0038':
        dict_seattle.append(measurement)
#print(dict_seattle)

# Part 1, 3
date_seattle = []
for date_code in dict_seattle:
    date = date_code['date']
    if date_split = date.split('-')
    date_seattle.append(measurement)
print(date_seattle)


total_precipitation = 0
for total in dict_seattle:
    total_precipitation += total['value']
#print(total_precipitation)


