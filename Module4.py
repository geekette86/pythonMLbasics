import pandas
from matplotlib import pyplot as plt
import numpy
filename= 'datastet/forestfires.csv'
names = ['X', 'Y', 'month', 'day', 'FFMC', 'DMC',
         'DC', 'ISI', 'temp', 'RH', 'wind','rain', 'area']
df = pandas.read_csv(filename,names=names)
#print(pandas.isnull(df))
print ("******************DataShape*******************")
print(df.shape)
print ("******************Data Types*******************")
print(df.dtypes)
print(df.head(1))
df.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),(1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
df.day.replace(('mon','tue','wed','thu','fri','sat','sun'),(1,2,3,4,5,6,7), inplace=True)
print("**************Inspecting the head of the data after replacement**************")
print(df.head(1))
print("**************Data Types Again**************")
print(df.dtypes)
print(df.describe())
print(df.corr(method='pearson'))
print("**************Data visualization**************")
# correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(df.corr(), vmin=-1, vmax=1, interpolation='none')
fig.colorbar(cax)
ticks = numpy.arange((0,13,1))
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.suptitle("Correlation Matrix",y=1.00,fontweight='bold')
plt.show()


