""" 
Data types: 
- Numbers (int, float, complex)
- Booleans (True and False)
- String
- List
- Set 
- Tuple
- Dictionary
"""

# Numbers
print(10, 100, -10, -5, 0)
print(9.81, 2.77, 3.14, 36.7)
print(1 + 2j, 4 + 3j, 4 + 5j , 10j)

# Booleans
print(True, False)
print(4 > 3, -1 < 0)
print(len('Finland') > len('Sweden'))

# Strings: a text under single, double or multiple quote. It could be one character or several pages

course = 'Data analysis with Python'
print(len(course))
print(course.upper())
print(course.lower())
print(course.swapcase())
print(course.title())
print(course.split())
print(course.startswith('Data'))
print('Py' in course)
print('land' in 'Finland')


first_name = 'Asabeneh'
last_name = 'Yetayeh'

# full_name = first_name + ' ' + last_name
full_name = f'{first_name} {last_name}'
print(full_name)
a = 3 
b = 4
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ^ {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')
