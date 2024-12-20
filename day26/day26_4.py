import pandas

weather_c = {
    'student': ['angela', 'yu', 'steve', 'colt'],
    "score": [12, 66, 25, 12],
    "height": [14, 66, 25, 12],
    "age": [15, 66, 25, 12],
    "weight": [14, 66, 25, 12],
    "fav_no": [21, 66, 25, 12],
    "birthday": [22, 66, 25, 12],
    "prevscore": [24, 66, 25, 12]
}

student_df = pandas.DataFrame(weather_c)

print(student_df)

for item in student_df:
    pass
    # print(item)

# for key, item in student_df.items():
#     print(key, item)
#     print("------------------")


for (key, item) in student_df.iterrows():
    # print(key, item)
    print("------------------")
    # print(key)
    # print(item)
    # print(item.student)
    # print(item.weight)
    if item.student == 'colt':
        print('##########', item.score, item.weight)


dict_new = {nkey: nvalue for nkey, nvalue in student_df.iterrows()}
print('++++++++++++++++', dict_new)

# with open('D:/documents/Python lessons/AngelaYu/day26/nato_phonetic_alphabet.csv') as nato:
#     print(nato)

nato_df = pandas.read_csv('D:/documents/Python lessons/AngelaYu/day26/nato_phonetic_alphabet.csv')
print(nato_df)

# diccct = nato_df.to_dict()
# print(diccct) # not what we want

# print(nato_df.letter, nato_df.code)

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
  

print(nato_dict)
 

name = input("name: ").upper()
nato = []
for l in name:
    nato.append(nato_dict[l])

print(nato)

nato2 = (nato_dict[i] for i in name + name) #use square bracket to get list, curly for dictionary and soecify key:value
print(nato2)
for _ in nato2:
    print(_)



# further investigation on this
nato_dict2 = [(key, value) for (key, value) in nato_df.iterrows()] 

print(nato_dict2)

for _ in nato_dict2:
    print(_)