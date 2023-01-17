import json
with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# Part 1, 2
seattle_list= []
for measurement in precipitation:
    station_code = measurement['station']
    if station_code == 'GHCND:US1WAKG0038':
        seattle_list.append(measurement)
#print(dict_seattle)

# Part 1, 3
months_sum_precipitation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for months in seattle_list:
    date = str(months['date'])
    date_split = date.split('-')
    month = date_split[1]
    month = int(month)
    index = month -1
    value = months['value']
    months_sum_precipitation[index] += value
print(months_sum_precipitation)

# Below is my process of thinking about EX.1.3
#x = range(12)
#precipitation_list = []
#for month in x:
#    month_value = []
#    precipitation_list.append(month_value)

#for date_seattle in dict_seattle:
#    date = str(date_seattle["date"])
#    date = date.split('-')
#    if date[1] == (f'0{month}') or (f'{month}'):
#        precipitation_list[month].append(date_seattle['value'])
#print(precipitation_list)

#months_dictionary = {'1':'0', '2':'0', '3':'0', '4':'0', '5':'0', '6':'0', '7':'0', '8':'0', '9':'0', '10':'0', '11':'0', '12':'0'}
#for dict_item in precipitation:
#    if dict_item['date'].startswith('2010-02'):
#        months_dictionary['2'] += (dict_item['value'])
#print(months_dictionary)


# .1.4
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(months_sum_precipitation, file, indent = 4)