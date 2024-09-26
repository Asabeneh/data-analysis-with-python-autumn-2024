# Functions: builtin function
# functions do have names, we call them, they take inputs
# print('love', 'people','python')

def do_something(value):
    print(f'I am {value}')

do_something('teaching')
do_something('learning')
do_something('playing football')
do_something('dancing')
do_something('coding')

def add_two_nums(x, y):
    total = x + y 
    return total 

print(add_two_nums(3, 4))
print(add_two_nums(30, 40))
print(add_two_nums(-3, 4))
print(add_two_nums(300, 700))
print(do_something('testing'))

def sum_of_evens(n):
    evens = list(range(0, n + 1, 2))
    total = sum(evens)
    return total
print(sum_of_evens(1000))

""" def calcuate_weight (mass, planet = ''):
    if planet == 'earth':
        return mass * 9.81
    elif planet == 'mars':
        return mass * 3.71
    elif planet == 'pluto':
        return mass * 0.62
    else:
        return mass * 1.62

print(calcuate_weight(75, 'earth'))
print(calcuate_weight(75)) """


def calcuate_weight (mass, gravity = 9.81):
    return mass * gravity

print(calcuate_weight(75))
print(calcuate_weight(75, 1.62))
    
def sum_of_all_nums(*args):
    return sum(args)
  

print(sum_of_all_nums(3, 10, -1, 20, 15))

def calc_volume_rect(w, l, h):
    return w * l * h

print(calc_volume_rect(w = 20, h  = 100, l = 15))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob','Tomi','Joh'))

def make_square (n):
    return n ** 2

print(make_square(10))

def make_cube(x, fn):
    return fn(x) * x

print(make_cube(10, make_square))

# Higher order functin is a function that takes an function as a parameter
# Higher order function is a function that return anothr function

# def do_math(x):
#     def add_ten():
#         return x + 10
#     return add_ten

def do_math(x):
    def add_ten():
        return x + 10
    def multiply():
        return x * 10
    return {
        'add_ten':add_ten,
        'multiply':multiply
    }

print(do_math(100))
print(do_math(100)['add_ten']())
print(do_math(100)['multiply']())
  