# File formats: txt, py, html, xml, json, csv, tsv, pdf, xaml
# Common file formats: csv, json, txt, 

f = open('./WEEK-6/notes.txt')
lines = f.readlines()
total_words = []
for line in lines:
    words = line.strip().lower().replace(':', ' ').replace(',', ' ').split()
    total_words.extend(words)
print(total_words)
f.close()
 
def word_count(filename):
    f = open(filename)
    lines = f.readlines()
    total_words = []
    for line in lines:
        words = line.strip().lower().replace(':', ' ').replace('.', ' ').replace(',', ' ').split()
        total_words.extend(words)
    f.close()
    return total_words
    
print(word_count('./data/donald_trump_speech.txt'))
