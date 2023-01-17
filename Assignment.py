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

x = range(12)
precipitation_list = []
for month in x:
    month_value = []
    precipitation_list.append(month_value)

for date_seattle in dict_seattle:
    date = str(date_seattle["date"])
    date = date.split('-')
    if date[1] == (f'0{month}') or (f'{month}'):
        precipitation_list[month].append(date_seattle['value'])
print(precipitation_list)

#month_sum = 0
#for month_value in month:
#    if month_value = [x]
#        month_sum += precipitation_list[]
#print(month_sum)