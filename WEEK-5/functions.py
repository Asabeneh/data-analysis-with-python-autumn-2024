# Functions:

def do_something(something):
    print(f'I am doing {something}')
    

do_something('teaching python')
do_something('learning python')
do_something('playing the guitar')
do_something('playing football')

'''

the name of the function will be print_fullname
it takes two parameters
it will print full name

'''

fullname = 'Asab Yetayeh'

def combine_names (first_name, last_name):
    fullname = f'{first_name} {last_name}'
    return fullname
fullname = combine_names('Asab','Yeta')

print(fullname + ' is a great Python teacher')
    
print(combine_names('Asab','Yeta'))
print(combine_names('Donlad', 'Trump'))
print(combine_names('John','Doe'))

fullname = combine_names('Donlad', 'Trump')
print(fullname + ' is a great leader')


def add_two_numbers(a, b):
    total = a + b 
    return total

print(add_two_numbers(1, 9))
print(add_two_numbers(2, 8))

def calculate_weight(mass, gravity = 9.81):
    '''
    Calculate a weight of a body. It take two numbers and returns the result.

    Args:
        mass (float): The first arg.
        gravity (float): The second arg.

    Returns:
        float: The product of mass and gravity.
    '''
    weight = mass * gravity
    return round(weight, 2),'N'
    
print(calculate_weight(74))
weight = calculate_weight(74)
print(type(weight))
print(calculate_weight(74.5, 3.71))
print(calculate_weight(74.5, 1.62))
print(calculate_weight.__doc__)

'''
function:calculate_circle_area 
paramter: radius
return area of a cirle 

pi * radius * radius

'''
# print(calculat_area_circle(10))
""" 
def calculate_area_circle(radius):
    PI = 3.14159
    area = PI * radius * radius 
    return area 

print(calculate_area_circle(10)) """


def calculate_area_circle(radius):
    PI = 3.14159
    return PI * radius ** 2
 

print(calculate_area_circle(10))

def do_what_ever(name, age, country, color, favorite, gender):
    return name, age, country, color, favorite, gender

print(do_what_ever(age = 250, name = 'Asab', country='Finland', gender ='Male',favorite='Python', color = 'Brown'))

print('Asab', 'Yeta', 2024, True, False, 'dkdkdkdk')

# Taking several arguments

""" def sum_all_numbers(*a):
    total = 0 
    for num in a:
        total = total + num 
    return total """

def sum_all_numbers(*args):
    return sum(args)

    
print(sum_all_numbers(1, 99, 10, 90, 800))

def generate_groups (team, *args):
    print(team, args)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob', 'Markku','Divya','Ankush'))

def kwarg_func(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    
    
kwarg_func(first_name = 'Asab', last_name = 'Yeta', age = 250, is_married = True, skills = ['Python','Data Analysis'])


def make_square(n):
    return n ** 2

print(make_square(3))
print(make_square(10))

square = lambda x: x ** 2
print(square(2))
print(square(10))

add_three_nums = lambda  x, y, z: x + y + z
print(add_three_nums(99, 1, 100))

''' 
a, b, c 
 2a + 3b + c


'''

linear_equation = lambda a, b, c: 2 * a + 3 * b + c


# Higher order function: is a function that take another function as a parameter
# Higher order function is a function that return other function

def make_square(n):
    return n ** 2 


def make_cube(n, make_square):
    return n * make_square(n)

print(make_cube(3, make_square))


def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return make_square
    elif type == 'cube':
        return make_cube
    elif type == 'absolute':
        return absolute
    
    
print(higher_order_function('square')(5))
print(higher_order_function('cube')(5, make_square))

    

