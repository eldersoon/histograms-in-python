import pandas as pd
import matplotlib.pyplot as plt

# import data set
data = pd.read_csv('variables.csv')

# show info about data set
# data.info()

# show data set
# print(data.head())

# data set description
# print(data.describe())

# build a histogram to V1 and V2 attributes:
# separate variables in x(V1) and y(V2)
x = data['V1']
y = data['V2']

# V1 Histogram
V1 = plt.figure(figsize=(7, 5))
xv1 = V1.add_subplot(1, 1, 1)
n, bins, patches = xv1.hist(x, color='pink')
xv1.set_xlabel('values V1 data set')
xv1.set_ylabel('Count')

# V2 Histogram
V2 = plt.figure(figsize=(7, 5))
xv2 = V2.add_subplot(1, 1, 1)
n, bins, patches = xv2.hist(y, color='purple')
xv2.set_xlabel('values V2 data set')
xv2.set_ylabel('Count')

# show both histograms
plt.show()







