import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
X, y = np.arange(10).reshape((5, 2)), range(5)
print ("Train Test Split")
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.33, random_state=5)
print("Xtrain")
print(X_train)
print("Xtest")
print(X_test)
print("Ytrain")
print(y_train)
print("Ytest")
print(y_test)
print ("Kfold Split ")
dataset=range(16)
KFCrossValidator = KFold(n_splits=5,shuffle=False)
KFdataset = KFCrossValidator.split(dataset)
print('{} {:^61} {}'.format('Round', 'Training set', 'Testing set'))
for iteration, data in enumerate(KFdataset, start=1):
    print('{:^9} {} {:^25}'.format(iteration, data[0], str(data[1])))
