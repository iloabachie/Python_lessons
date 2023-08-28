import csv
import datetime

path = r"D:\Documents\Python lessons\AngelaYu\Google Stock Market Data.csv"
    
with open(path, newline='') as datafile:
    data_list = [line.strip().split(",") for line in datafile] # normal opening    
print(data_list[0])
for _ in range(10):
    print(data_list[_])

print("_"*10)  
# the CSV option
file = open(path, newline='')
datareader = csv.reader(file)  


data = []
for row in datareader:
    # print(row)
    if row == ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']:
        continue
    date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
    openp = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj = float(row[6])
    data.append([row[0], openp, high, low, close, volume, adj])
    # print([row[0], openp, high, low, close, volume, adj])
    
for i in range(10):
    # print(data[i]) 
    ...

# =====================

data = [
    ["Date", "Open", "Close", "Return"],
    ["2023-07-15", 100.0, 105.0, 5.0],
    ["2023-07-16", 105.0, 110.0, 5.0],
]

filename = "output.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to {filename}.")

# +++++++++++++++++++++++++++++++

# compute and store daily stock returns
return_path = r"Algorithm\daily_returns.csv"
return_file = open(return_path, "w", newline='')
writer = csv.writer(file)

writer.writerow(["Date", "Open", "Close", "Return"])

for row in data:
    date = row[0]
    openp = row[1]
    closep = row[4]
    diff = closep - openp
    
    writer.writerow([date, openp, closep, diff])



datadict = csv.DictReader(return_file)

file.close()
return_file.close()

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        e=enumerate(nums)
        return [[a, b, c, d] for i, a in e for j, b in e for k, c in e for l, d in e if len(set([i,j,k,l]))==4 and a+b+c+d == target]
    

