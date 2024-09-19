
a = 5

if a > 0:
    print('The number is positive')
elif a < 0:
    print('The number is negative')
else:
    print('the number is zero')

is_raining = False 

if is_raining:
    print('Go out with an umbrella')
else:
    print('Go out freely it is a shinny day!')
""" 
weather = input('What is the weather today? ').lower()

if weather == 'rainy':
    print('Go with an unbrella or a raincoat')
elif weather == 'cloudy':
    print('It may rain and consider a raincoat')
elif weather == 'snowy':
    print('It may be slippery')
elif weather == 'foggy':
    print('Visiblity might be hindered')
elif weather == 'sunny':
    print('It is a great day to go to the beach')
else:
    print('No one knows about the weather')

print('test it') """

weather = input('What is the weather today? ').lower()
match weather:
    case 'rainy':
        print('Go with an unbrella or a raincoat')
    case 'cloudy':
        print('It may rain and consider a raincoat')
    case 'snowy':
        print('It may be slippery')
    case 'foggy':
        print('Visiblity might be hindered')
    case 'sunny':
        print('It is a great day to go to the beach')
    case _:
        print('No one knows about the weather') 


