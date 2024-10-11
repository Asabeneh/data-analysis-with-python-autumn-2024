# 
import datetime
now = datetime.datetime.today()
print(now)


f = open('sample.txt', 'a')

f.write(str(now) + '- I hope you love the python programming\n')

