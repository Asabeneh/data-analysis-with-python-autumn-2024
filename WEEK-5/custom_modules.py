def do_something(something):
    print(f'I am doing {something}')
    
def combine_names (first_name, last_name):
    fullname = f'{first_name} {last_name}'
    return fullname

def calculate_area_circle (radius):
    import math
    PI = math.pi 
    return round(PI * radius ** 2, 2)
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
    return round(weight, 2)

def make_square(n):
    return n ** 2