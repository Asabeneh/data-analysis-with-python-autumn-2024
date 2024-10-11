# map, filter, reduce
# map => [1, 2, 3, 4,5] => [11, 12, 13, 14, 15]

from pprint import pprint
from countries_data import countries_data
from functools import reduce

nums = [1, 2, 3, 4, 5]

""" new_lst = []

for num in nums:
    new_lst.append(num + 10)
    
print(new_lst) """


doubled_nums= list(map(lambda x: x * 2, nums))
print(doubled_nums)

country_names = []
cities = []
for country in countries_data:
    country_names.append(country['name'])
    cities.append(country['capital'])
    
print(country_names)
print('---- cities ---')
print(cities)

country_names = list(map(lambda country: country['name'], countries_data))
capitals = list(map(lambda country: country['capital'], countries_data))
populations = list(map(lambda country: country['population'], countries_data))

countries = ['Finland','Sweden','Denmark','Norway','Iceland']

pprint(list(map(lambda country: {'country':country, 'country_cap':country.upper(), 'country_code':country.upper()[:3]}, countries)))

# Filter 

nums = [-5, -3, 0, 1, 4, 8, 2, 0.5, -10,  6]

""" evens = []
for num in nums:
    if num % 2 == 0 and num > 0:
        evens.append(num)
print(evens) """

evens = list(filter(lambda n: n % 2 == 0 and n > 0, nums))

countries_with_land = list(filter(lambda country: 'land' in country, country_names))
pprint(countries_with_land)


# Reduce -> 

nums = [-5, -3, 0, 1, 4, 8, 2, 0.5, -10,  6]

total = 0 
for num in nums:
    total = total + num

total = reduce(lambda acc, cur: acc * cur, nums, 1)
print(total)


world_population = reduce(lambda acc, current: acc + current['population'],  countries_data, 0)
print(world_population)

# map -> filter -> reduce

