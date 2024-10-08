# string: any text under single, double or triple quote is a stirng

letter = 'a'
print(type(letter), len(letter))
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets, len(alphabets))
print(list(alphabets))
lang = 'Python'
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])
print(len(lang))
last_index = len(lang) - 1
print(lang[last_index])
print(lang[-6])
print(lang[-1])
print(alphabets[-1])


# slicing
print(lang[0:2])
print(lang[2:5])

print(alphabets[0:5])
print(alphabets[:5])
print(alphabets[5:26])
print(alphabets[5:])
print(lang[-4:-1])
print(alphabets[-1])

last_index = len(alphabets) - 1
print(alphabets[last_index])

# String Methods: upper, lower, title, 
print(dir('dkdkdkdkkdkdkdkdkdk'))

""" string_methods = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """
# print(len(string_methods))

txt = 'Python for everyone'
print(len(txt))
print(txt.split())
print(txt.capitalize())
print(txt.upper())
print(txt.lower())

print('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'.startswith('From'))
print('From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'.split())

txt = '  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

does_it_start_with_from = txt.strip().startswith('From')
if does_it_start_with_from:
    txt = txt.split()
    print(txt, txt[1])

txt = 'Python for everyone'
print(txt.title())
print(txt.endswith('e'))
print(txt.find('y'))
print(txt.rfind('y'))

print(txt.index('P'))
print(txt.index('y'))
print(txt.rindex('y'))

if 'Pp' in txt:
    print(txt.index('Pp'))
else:
    print('Not found')
print(txt, txt.count('o'))

dna = '''CTAGCAAACTGCTGATCCAGTTTAACTCACCAAATTATAGCCGTACAGACCGAAATCTTAAGTCATATCACGCGACTAGCCTCTGCTTAATTTTTGTGCTCAAGGGTTTTGGTCCGCCCGAGCGGTGCAGCCGATTAGGACCATGTAATACATTTGTTACAAGACTTCTTTTAAACACTTTCTTCCTGCCCAGTAGCGGATGATAATCGTTGTTGCCAGCCGGCGTGGAAGGTAACAGCACCGGTGCGAGCCTAATGTGCCGTCTCCACGAACACAAGGCTGTCCGATCGTATAATAGGATTCCGCAATGGGGTTAGCAAGTGGCAGCCTAAACGATATCGGGGACTTGCGATGTACATGCTTTGGTACAATACATACGTGATCCAGTTGTTATCCTGCATCGGAACATCAATTGTGCATCGGACCAGCATATTCATGTCATCTAGGAGGCGCGCGTAGGATAAATAATTCAATTAAGATGTCGTTTTGCTAGTATACGTCTAGGCGTCACCCGCCATCTGTGTGCAGGTGGGCCGACGAGACACTGTCCCTGATTTCTCCGCTTCTAATAGCACACACGGGGCAATACCAGCACAAGCCAGTCTCGCAGCAACGCTCGTCAGCAAACGAAAGAGCTTAAGGCTCGCCAATTCGCACTGTCAGGGTCGCTTGGGTGTTTTGCACTAGCGTCAGGTACGCTAGTATGCGTTCTTCCTTCCAGGGGTATGTGGCTGCGTGGTCAAATGTGCGGCATACGTATTTGCTCGACGTGTTTGCTCTCACGAACTTGACCTGGAGATCAAGGAGATGTTTCTTGTCGAACTGGACAGCGCTTCAACGGAACGGATCTACGTTACAGCCTGCATAATGAAAACGGAGTTGCCGACGACGAAAGCGACTTTGGGTTCTGTCTGTTGTCATTGGCGGAAAACTTCCGTTCAGGAGGCGGACACTGATTGACACGGTTTAGCAGAAGGTTTGAGGAATAGGTTAAATTGAG'''
# C T A G 

total = len(dna)
print(total)
a = dna.count('A')
c = dna.count('C')
t = dna.count('T')
g = dna.count('G')
print(a / total, c / total, t / total, g /total)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250 
country = 'Finland'
city = 'Helsinki'

full_name = first_name + ' ' + last_name 
print(full_name)
print(f'I am {first_name} {last_name}. I am {age} years old. I live in {country}, {city}.')
print('I am {} {}. I am {} years old. I live {}, {}.'.format(first_name, last_name, age, country, city))
print('I love {} {}.'.format('water', 'melon'))


# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
age = 250
height = 1.71345
formated_string = 'I am %s %s. I teach %s. I am %d years old. I am not short as you think, %.2f meters' %(first_name, last_name, language, age, height)
print(formated_string)

formated_string = f'I am {first_name} {last_name}. I teach {language}. I am {age} years old. I am not short as you think {height:.2f} meters'
print(formated_string)

language = 'Python'
print(language.isupper())

print('Asab','Yeta', 2024, sep='\n')
print('\tI love People.\n\tI love Python to')
print('=o==o====o=====o====o=====')
print('-----------------------------')
print()
print('Week 1 \tWeek 2 \t Week 3')
print('5 \t32 \t 10')

print('I love people. The love of people killing.'.replace('love', 'like'))

donald_speech = '''
Chief Justice Roberts, President Carter, President Clinton, President Bush, fellow Americans and people of the world – thank you.
 We the citizens of America have now joined a great national effort to rebuild our county and restore its promise for all our people.
Together we will determine the course of America for many, many years to come.
Together we will face challenges. We will confront hardships. But we will get the job done.
Every four years we gather on these steps to carry out the orderly and peaceful transfer of power.
And we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent, thank you.
Today’s ceremony, however, has very special meaning because today we are not merely transferring power from one administration to another – but transferring it from Washington DC and giving it back to you the people.
For too long a small group in our nation’s capital has reaped the rewards of government while the people have borne the cost.
Washington flourished but the people did not share in its wealth. Politicians prospered but the jobs left and the factories closed.The establishment protected itself but not the citizens of our country.
Their victories have not been your victories. Their triumphs have not been your triumphs. While they have celebrated there has been little to celebrate for struggling families all across our land.
That all changes starting right here and right now because this moment is your moment. It belongs to you. It belongs to everyone gathered here today and everyone watching all across America today.
This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people.
Today, January 20 2017, will be remembered as the day the people became the rulers of this nation again.The forgotten men and women of our country will be forgotten no longer. Everyone is listening to you now.
You came by the tens of millions to become part of a historic movement –  the likes of which the world has never seen before.
At the centre of this movement is a crucial conviction – that a nation exists to serve its citizens.Americans want great schools for their children, safe neighbourhoods for their families and good jobs for themselves.
These are just and reasonable demands.Mothers and children trapped in poverty in our inner cities, rusted out factories scattered like tombstones across the landscape of our nation.
An education system flushed with cash, but which leaves our young and beautiful students deprived of all knowledge. And the crime and the gangs and the drugs which deprive people of so much unrealised potential.
We are one nation, and their pain is our pain, their dreams are our dreams, we share one nation, one home and one glorious destiny.
Today I take an oath of allegiance to all Americans. For many decades, we’ve enriched foreign industry at the expense of American industry, subsidised the armies of other countries, while allowing the sad depletion of our own military.
We've defended other nations’ borders while refusing to defend our own.And spent trillions and trillions of dollars overseas while America’s infrastructure has fallen into disrepair and decay.
We have made other countries rich while the wealth, strength and confidence of our country has dissipated over the horizon.
One by one, shutters have closed on our factories without even a thought about the millions and millions of those who have been left behind.
But that is the past and now we are looking only to the future.
We assembled here today are issuing a new decree to be heard in every city, in every foreign capital, in every hall of power – from this day on a new vision will govern our land – from this day onwards it is only going to be America first – America first!
Every decision on trade, on taxes, on immigration, on foreign affairs will be made to benefit American workers and American families.
Protection will lead to great prosperity and strength. I will fight for you with every bone in my body and I will never ever let you down.
America will start winning again. America will start winning like never before.
We will bring back our jobs, we will bring back our borders, we will bring back our wealth, we will bring back our dreams.
We will bring new roads and high roads and bridges and tunnels and railways all across our wonderful nation.
We will get our people off welfare and back to work – rebuilding our country with American hands and American labour.
We will follow two simple rules – buy American and hire American.
We see good will with the nations of the world but we do so with the understanding that it is the right of all nations to put their nations first.
We will shine for everyone to follow.We will reinforce old alliances and form new ones, and untie the world against radical Islamic terrorism which we will eradicate from the face of the earth.
At the bed rock of our politics will be an allegiance to the United States.And we will discover new allegiance to each other. There is no room for prejudice.
The bible tells us how good and pleasant it is when god’s people live together in unity.When America is united, America is totally unstoppable
There is no fear, we are protected and will always be protected by the great men and women of our military and most importantly we will be protected by god.
Finally, we must think big and dream even bigger. As Americans, we know we live as a nation only when it is striving. 
We will no longer accept politicians who are always complaining but never doing anything about it.The time for empty talk is over, now arrives the hour of action.
Do not allow anyone to tell you it cannot be done. No challenge can match the heart and fight and spirit of America. We will not fail, our country will thrive and prosper again.
We stand at the birth of a new millennium, ready to unlock the mysteries of space, to free the earth from the miseries of disease, to harvest the energies, industries and technologies of tomorrow.
A new national pride will stir ourselves, lift our sights and heal our divisions. It’s time to remember that old wisdom our soldiers will never forget, that whether we are black or brown or white, we all bleed the same red blood of patriots.
We all enjoy the same glorious freedoms and we all salute the same great American flag and whether a child is born in the urban sprawl of Detroit or the windswept plains of Nebraska, they look at the same night sky, and dream the same dreams, and they are infused with the breath by the same almighty creator.
So to all Americans in every city near and far, small and large, from mountain to mountain, from ocean to ocean – hear these words – you will never be ignored again.
Your voice, your hopes and dreams will define your American destiny.Your courage, goodness and love will forever guide us along the way.
Together we will make America strong again, we will make America wealthy again, we will make America safe again and yes – together we will make America great again.
Thank you.
God bless you.
And god bless America.
'''


words = donald_speech.lower().replace('–', ' ').replace('.', ' ').replace('?', ' ').split()
print(words)
print(len(words))
unique_words = set(words)
print(len(unique_words))