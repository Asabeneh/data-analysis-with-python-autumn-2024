from countries_data import countries_data as data
from pprint import pprint
nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]


doubled = [ num + 10 for num in nums]
print(doubled)

nums = [-5, -3, 0, 1, 4, 8, 2, 0.5, -10,  6]

evens = [num for num in nums if num % 2 == 0]
print(evens)
country_names = [country['name'] for country in data ]
print(country_names)

country_with_land = [country['name'] for country in data if 'land' in country['name']]
print(country_with_land)


tranformed_data = [{
    'name':country['name'],
    'capital':country['capital'], 
    'population':country['population']
    } for country in data ]

pprint(tranformed_data)

lst_of_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

new_lst = []
for l in lst_of_lst:
    new_lst.extend(l)
print(new_lst)

print([l for lst in lst_of_lst for l in lst])

from countries_data import countries_data as countries

# languages =set([languages for country in countries for languages in country['languages']])

# print(languages)
languages_lst = []
for country in countries:
    languages = country['languages']
    languages_lst.extend(languages)
    
print(languages_lst, len(languages_lst))
languages_set = set(languages_lst) # removing duplicates
print(len(languages_set))

languages_lst = [language for country in countries for language in country['languages']]
number_of_languages = len(set(languages_lst))
    
