import json

with open('words.json') as words:
    word_data = json.load(words)

#print(word_data[0])

#print(word_data[0]['word'])

for data in word_data:
    #print(data['word'])
    if data['part of speech'] == 'verb':
        print(data['word'])
        
#count how many nouns
num_nouns = 0
for data in word_data:
    if data['part of speech'] == 'noun':
        num_nouns+=1 #num_nouns++ idn't valid Python syntax
print(num_nouns)