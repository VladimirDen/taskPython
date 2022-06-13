dict_str = {}
d = []
r1 = []
r = []
input_list = []
list_input = []
dictionary_en = open('task2/input.txt', 'r', encoding='utf-8')
dict_list = dictionary_en.readline()

while dict_list != '':
    dict_list = dict_list.strip()
    d = dict_list.split(":")
    r.append(tuple(d))
    dict_list = dictionary_en.readline()
print(r)
"""for i in r:
    if ',' in i[1]:
        r.remove(i)
        m = list(i)
        k = i[1].split(",")
        m.remove(i[1])
        m.append(k)
        r.append(tuple(m))
    else:
        continue
print(*r, sep='\n')
#for i in range(3):"""
