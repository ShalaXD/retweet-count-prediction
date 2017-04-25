# Shala Chen
# MSE: 1333062.04

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

# import and separate data sets
csv = np.genfromtxt('newData.csv', delimiter=",")
classescsv = np.genfromtxt('classes.csv',delimiter=",")
data = csv[1:,:]
classes = classescsv[1:]
train_data = data[0:140000]
train_label = classes[0:140000]
test_data = data[140000:154515]
test_label = classes[140000:154515]

# Build and train the model using the training sets
logModel = linear_model.LogisticRegression(C=1e5)
logModel.fit(train_data, train_label)

# Predict rts_likes using testing sets
output = logModel.predict(test_data)
var = np.mean(abs(output - test_label)**2)

#print('Coefficients: \n', logModel.coef_)
print("Mean squared error: %.2f" % np.mean(( output - test_label) ** 2))
print('Variance score: %.2f' % logModel.score(test_data, test_label))



