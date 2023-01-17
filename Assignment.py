import json
with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# PART 1, 2
seattle_list= []
for measurement in precipitation:
    station_code = measurement['station']
    if station_code == 'GHCND:US1WAKG0038':
        seattle_list.append(measurement)
print(seattle_list)

# PART 1, 3
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
# --------
#for date_seattle in dict_seattle:
#    date = str(date_seattle["date"])
#    date = date.split('-')
#    if date[1] == (f'0{month}') or (f'{month}'):
#        precipitation_list[month].append(date_seattle['value'])
#print(precipitation_list)
# ----------
#months_dictionary = {'1':'0', '2':'0', '3':'0', '4':'0', '5':'0', '6':'0', '7':'0', '8':'0', '9':'0', '10':'0', '11':'0', '12':'0'}
#for dict_item in precipitation:
#    if dict_item['date'].startswith('2010-02'):
#        months_dictionary['2'] += (dict_item['value'])
#print(months_dictionary)


# PART 1, 3
Seattle = {
    "Seattle": {
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": months_sum_precipitation
        #"total_yearly_precipitation": ...,
        #"relative_monthly_precipitation": [...],
        #"relative_yearly_precipitation": ...
    }
}
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Seattle, file, indent = 4)

# PART 2, 1
total_yearly_precipitation = 0
for total_sum in seattle_list:
    total_yearly_precipitation += total_sum['value']
print(total_yearly_precipitation)

# PART 2, 2
relative_monthly_precipitation = []
for monthly_precipitation in months_sum_precipitation:
    relative_ratio = monthly_precipitation/total_yearly_precipitation
    rounded_ratio = round(relative_ratio, 2)
    relative_monthly_precipitation.append(rounded_ratio)
print(relative_monthly_precipitation)

# PART 2, 3
Seattle = {
    "Seattle": {
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": months_sum_precipitation,
        "total_yearly_precipitation": total_yearly_precipitation,
        "relative_monthly_precipitation": relative_monthly_precipitation,
        #"relative_yearly_precipitation": ...
    }
}
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Seattle, file, indent = 4)

# PART 3, 1
from csv import DictReader
with open('stations.csv') as file:
    reader = DictReader(file)
    items = list(reader)

def calculate_monthly(station_code):
    # calculate the totals per month for states
    total_precipitation_monthly = [0] * 12
    for measurement in precipitation:
        if measurement['station'] == station_code:
            date_split = measurement['date'].split('-')
            month = int(date_split[1])
            total_precipitation_monthly[month -1] += measurement['value']

    #calculating the total over the whole year
    yearly_precipitation_total = sum(total_precipitation_monthly)

    #calculating the relative percentages per month
    relative_monthly_precipitation_other = []
    for monthly_precipitation_other in total_precipitation_monthly:
        relative_monthly_precipitation_other.append(monthly_precipitation_other/yearly_precipitation_total)

calculate_monthly('GHCND:US1CASD0032')
print(calculate_monthly)
# return <function calculate_monthly at 0x10108e5c0>, and I'm not sure what this exactly means :((