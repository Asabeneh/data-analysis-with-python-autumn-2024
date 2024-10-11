import json 
from pprint import pprint

f = open('python_libraries.json', encoding='utf-8')
data = json.load(f)
for item in data:
    pprint(item)
f.close()
    
with  open('python_libraries.json', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        print(item['use_cases'], item['name'])
    