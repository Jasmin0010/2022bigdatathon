import csv
from pandas import Series, DataFrame
with open("MBTI_train.csv", 'r') as raw:
    lines = raw.readlines()
data_temp = csv.reader(lines)
data = []
for record in data_temp:
    data.append(record)
    
df = DataFrame(data[1:])
df.columns = ['TYPE','DESCRIPTION']

df.head()