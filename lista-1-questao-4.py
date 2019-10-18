import csv
import pandas as pd

# 4 - create a data set contains two variables V1 and V2:
# where V1 median < V1 mean and V2 median > V2 mean:

# create data csv
csvData = [
    ['V1', 'V2'],
    [3, 21],
    [1, 21],
    [1, 21],
    [1, 23],
    [2, 18],
    [2, 19],
    [4, 18],
    [1, 28],
    [1, 24],
    [2, 22],
    [3, 22],
    [2, 21],
    [1, 18],
    [4, 21],
    [2, 19],
    [2, 20],
    [3, 19],
    [2, 17],
]
# create a csv file:
with open('variables.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()

data = pd.read_csv('variables.csv')

# show data set in csv format:
# print(data)

# calculate V1's mean and median:
meanV1 = data['V1'].mean()
medianV1 = data['V1'].median()

# calculate V1's mean and median:
meanV2 = data['V2'].mean()
medianV2 = data['V2'].median()

# show V1's mean and median
print("Mean: ", meanV1, "Median: ", medianV1)

# show V2's mean and median
print("Mean: ", meanV2, "Median: ", medianV2)

# return boolean value
print("V1 median < V1 mean : ", medianV1 < meanV1)
print("V2 median > V2 mean:", medianV2 > meanV2)
