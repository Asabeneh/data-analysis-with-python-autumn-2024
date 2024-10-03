# # 
# import math 
from math import pi, sqrt, factorial as f, log10, e, floor, ceil
# from math import *


math_module_methods = ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# 5! = 5 * 4 * 3 * 4 * 1 = 120
# 2 ^ 1/2 = 
print(f(5))
print(sqrt(2), 2 ** 0.5 )
print(pi)
print(log10(1000))
print(e)
def calculate_area_circle (radius):
    PI = math.pi 
    return PI * radius ** 2

from random import randint, choice, shuffle, random

lst = ['betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random())

print(floor(9.81))
print(floor(3.14))
print(ceil(3.14))
print(ceil(9.81))
print(floor(random() * 11))  # 0 to 10
print(randint(0, 10))
print(choice('aeiou'))

lst = [1, 2, 'milk', 4, 5]
shuffle(lst)
print(lst)