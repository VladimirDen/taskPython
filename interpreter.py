import re
dict_str = {}
d = []
r = []
input_list = []
list_input = []
dictionary_en = open('task1/en_ru.txt', 'r', encoding='utf-8')
dict_list = dictionary_en.readline()

while dict_list != '':
    dict_list = dict_list.strip()
    d = re.split("\t-\t", dict_list)
    r.append(tuple(d))
    dict_str = {x: y for x, y in r}
    dict_str.update(dict_str)
    dict_list = dictionary_en.readline()

file_input = open('task4/input.txt', 'r', encoding='utf-8')
file_input_str = file_input.readline()

while file_input_str != '':
    file_input_str = file_input_str.strip().lower()
    list_input = re.split(r'\W+', file_input_str)
    input_list.append(list_input)
    file_input_str = file_input.readline()

for str_word in input_list:
    for word in str_word:
        if word in dict_str:
            recording = open('output.txt', 'a', encoding='utf-8')
            recording.write(dict_str[word] + '\n')
            recording.close()
        else:
            recording = open('output.txt', 'a', encoding='utf-8')
            recording.write(word + '\n')
            recording.close()
