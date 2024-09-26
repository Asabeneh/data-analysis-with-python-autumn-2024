
print(list(range(1, 5, 2)))

# integers: negatives, zero, positives
# -3, -2, -1, 0, 1, 2, 3, 4
""" even_nums = []
odd_nums = []
for i in range(101):
    if i % 2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
print('even numbers:', even_nums)
print('odd numbers ', odd_nums)

evens = list(range(0, 51, 2))
print(evens, sum(evens))

for i in range(10, -1, -1): # 10 to 0
    print(i)

integers = []
for i in range(-100, 101, 1):
    integers.append(i)
print('integers: ', integers) """

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

new_lst = []
for country in countries:
    # print(country, len(country), country.upper(), country.upper()[:3])
    # new_lst.append([country, len(country),  country.upper(),  country.upper()[:3]])
     new_lst.append(country.upper())

# print(new_lst)

# for item in new_lst:
#     print(item)

countries_with_more_words = []
for country in countries:
     words = country.split()
     if len(words) >= 2:
          countries_with_more_words.append(country)

print(countries_with_more_words)

length = len(countries)
middle_index = length // 2
middle_country = countries[middle_index]
print(middle_country)

""" nums = [1, 2, 3, 4, 5] # middle = > 3, index = 2
length = len(nums) # 5 
middle_index = length // 2
print(middle_index)
print(nums[middle_index]) """


from pprint import pprint
# import countries_data
from countries_data import countries_data

""" world_population = 0
for country in countries_data:
     population = country['population']
     world_population = world_population + population
print(world_population) """

""" new_lst = []
for country in countries_data:
     name = country['name']
     population = country['population']
     capital = country['capital']
     new_lst.append([name, capital, population])
pprint(new_lst)
 """


# for, while, do while  for of for in , forEach
# for _ in range(101):
#      print('I will love Python')


# While Loop

count = 0

while count < 11:
     print(count)
     count = count + 2



""" ages = []
while True:
    age = int(input('Enter age: '))
    print(age)
    if age < 19:
         break 
    elif age < 0:
         break 
    else:
         # TODO TASK
         pass
    ages.append(age)
    
print(ages) """

# 10 to 0 in while

i = 10

while i >= 0:
     print(i)
     i = i - 1
print('dldldldl')

nums = [2, -4, 3, 7, -9, 9.8, 2.77, 10, -5, 8]

print(' === with continue ====')
for num in nums:
     if num < 0:
          continue
     print(num)

print('==== with some conditon ===')
for num in nums:
     if num > 0:
          print(num)

print('=== all the evens in the list')
for num in nums:
     if num % 2 == 0:
          print(num)


print('=== positive even numbers ===')
for num in nums:
     if num % 2 == 0 and num > 0:
          print(num)


print('break if there is a negative number')
for num in nums:
     if num < 0:
          break
     print(num)


count  = 0

while count < 10:
     print(count)
    #  count = count + 1
