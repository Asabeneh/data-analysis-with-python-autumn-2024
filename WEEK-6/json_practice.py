import json
from countries_data import countries_data as data
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)


# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
countries = [{
    'name':country['name'],
    'capital':country['capital'],
    'population':country['population'],
    'flag':country['flag']
} for country in data]
with open('./data/countries.json', 'w', encoding='utf-8') as f:
    json.dump(countries, f, ensure_ascii=False, indent=4)
    
def generate_json_file(filename, data):
    import json
    with open(f'./data/{filename}', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
generate_json_file('test.json', countries)