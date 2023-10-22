import pandas as pd

df = pd.read_csv('D:\documents\Python lessons\AngelaYu\day25\Squirrel_Data.csv')

print(type(df.describe()))

# with open('D:\documents\Python lessons\AngelaYu\day25\describe.txt', mode='w') as desc:
#     desc.write(df.describe())

df.describe().to_csv('D:\documents\Python lessons\AngelaYu\day25\describe.csv')

print(df.head())

print(df['Primary Fur Color'])
list = df.X.to_list()
# print(list)

print(df['Primary Fur Color'].value_counts())

df['Primary Fur Color'].value_counts().to_csv('D:\documents\Python lessons\AngelaYu\day25\squirrel_count.csv')