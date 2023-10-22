# with open('D:\documents\Python lessons\AngelaYu\day25\weather_data.csv') as weather:
#     data = weather.readlines()
#     print(data)
#     data = [day.strip() for day in data]
#     print(data) #out put needs a lot of cleaning


# tricky to handle so we use pandas

import csv # just to get a simple column of data.  inbuilt package easier with pandas

with open('D:\documents\Python lessons\AngelaYu\day25\weather_data.csv') as weather:
    data = csv.reader(weather)
    # print(data) # prints an object
    # for row in data:
    #     print(1, row)   
    temperatures = []
    print(33, data)
    for r in data:
        # print(2, row[1])
        if r[1] != 'temp':        
            temperatures.append(int(r[1]))  #so many line just to get the data in a column
    
    print(temperatures)

# --------------------------------------------------------------------
import pandas

data = pandas.read_csv('D:\documents\Python lessons\AngelaYu\day25\weather_data.csv')

print(data)
print("*******************", data['temp']) # easier to get column data

dict = data.to_dict()

print(dict)

temp_list = data['temp'].to_list()
print(temp_list)

avg = sum(temp_list) / len(temp_list)

print(avg)

avg2 = data['temp'].mean()
avg3 = data.temp.mean()

print(222, avg3)

maxi = data['temp'].max()
print(maxi)

# get data in row

print(data[data.day == 'Monday'], 'CHECK THIS')
print(data.head(3))
print(data.describe())

print(data[data.temp == data.temp.max()])

print(data[data.condition == 'Sunny'])

sunny = data[data.condition == 'Sunny']

print(99, sunny.condition)


mon = data[data.day == 'Monday']
print(88888, int(mon.temp))
print(88888, (mon.temp))


# -----------------------
# create a data frame form scratch

data_dict = {
    'students': ['amy', 'john', 'sesan', 'bill'],
    'scores': [77, 56, 78, 12],
    "Wednesday": [15, 66, 25, 12]
}

weather_c = {
    'time': ['morning', 'afternoon', 'evening', 'night'],
    "Monday": [12, 66, 25, 12],
    "Tuesday": [14, 66, 25, 12],
    "Wednesday": [15, 66, 25, 12],
    "Thursday": [14, 66, 25, 12],
    "Friday": [21, 66, 25, 12],
    "Saturday": [22, 66, 25, 12],
    "Sunday": [24, 66, 25, 12],
}

new_data = pandas.DataFrame(data_dict)
new_data2 = pandas.DataFrame(weather_c)

print("###\n", new_data2)

new_data.to_csv('newcsv.csv')

data2 = pandas.read_csv('D:\documents\Python lessons\AngelaYu\day25\pokemon_data.csv')
print(data2.describe())

print(data2.head())