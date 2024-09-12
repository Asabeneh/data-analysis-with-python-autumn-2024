'''
Function is a block of code the allow as to solve problem or task.
There are two types of functions:
- Builtin Functions
- Custom Function

Most common builtin functions:
- print
- len
- type
- int, str, float
- input
- range
- list, set, dict, tuple
- round
- abs
- dir
- min, max, sum
- enumerate

'''

# a print builtin function allow us to dispay a different data types

print(10, type(10))
print(9.81, type(9.81))
print(1+ 2j, type('Asabeneh'))
print(True, type(True))

print('Asabeneh Yetayeh', 'Finland', 'Helsink', 250, ['HTML','CSS','JS'], sep = "          ")
print('Asabeneh Yetayeh', 'Finland', 'Helsink', 250, ['HTML','CSS','JS'], sep = ", ")
print('Asabeneh Yetayeh', 'Finland', 'Helsink', 250, ['HTML','CSS','JS'], sep = "\n")
print('> Asabeneh Yetayeh', 'Finland', 'Helsink', 250, ['HTML','CSS','JS'], sep = "\n> ")

# Len function give the length of any sequence 

print(len('cat'))
print(len('Finland'))
print(len('i love you'))

# type - allow us to know the data type of  a data

print(10, type(10))
print(9.81, type(9.81))
print(1 + 4j, type(1 + 4j))

print(10, '10', type(10), type('10'))
print('10' + str(10))
print(10 + int('10'))
print('love' * 3)
print(float('9.81') * 75.5) # wieght = mass * gravity
print(round(float('9.81') * 75.5, 1))
print(round(float('9.81') * 75.5))

# input allow as to get data from user

"""
name = input('Enter you name ')
birth_year = input('When were you born? ')

age = 2024 - int(birth_year)

print(age)



"""


# range create range of integers from start to an end point, it has also step

# range(start, end, step)
print(range(0, 10, 1))

print(list())
print(list('cat'))
print(list(range(0, 11, 1)))

print(list(range(0, 101, 1)))

print(list(range(0, 101, 2)))
print(list(range(1, 101, 2)))

# Data type: number(int, float, complex), boolean, string, list, set, tuple, dictionary 
print([])
print(list())
print(type([]), type([1,2,3,4]), len([1, 2,3,4]))
print(['Milk','Meat','Coffee','Honey','Sugar'], len(['Milk','Meat','Coffee','Honey','Sugar']))
print(set())
print({1, 2, 3,3, 3,4,4})
print(['English','French','Finnish','Swedish','Finnish','English','Spanish'])
languages_lst = ['English','French','Finnish','Swedish','Finnish','English','Spanish']
languages_set = set(languages_lst)
print(languages_set, len(languages_set))
print(set(['English','French','Finnish','Swedish','Finnish','English','Spanish']), len(set(['English','French','Finnish','Swedish','Finnish','English','Spanish'])))
print((1, 2, 3,4), type((1,2,3,4)))
print(dict(), {}, type({}), {'name':'asab','age':250})
print(type({

    'rouka':'food',
    'tietokone':'computer',
    'tuoli':'chair',
    'kirja':'book'
}))
print("3 - 5".split(' - '), type("3 - 5"))
lst = "3 - 5".split(' - ')
print(lst)
# mn = lst[0]
# mx = lst[1]
mn, mx = lst
print(mn, mx, type(mn), type(mx))
print( (int(mn) + int(mx)) / 2)

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']

fin, sw,*rest = countries
print(fin, sw,rest)
print(abs(-5))
print(min(-2, 10, 5, 20, 100, -20))
print(max(-2, 10, 5, 20, 100, -20))
print(sum([-2, 10, 5, 20, 100, -20]))

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']
print(list(enumerate(countries)))

print(dir('dkdkddkdkdkdkdkdk'))
print('there is nothing like love in this world, that is why i love every one'.count('i'))