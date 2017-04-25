# Shala Chen
# Mean squared error: 801897.87

import numpy as np
from sklearn import datasets, linear_model

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
lrModel = linear_model.LinearRegression()
lrModel.fit(train_data, train_label)

# Predict rts_likes using testing sets
output = lrModel.predict(test_data)
var = np.mean(abs(output - test_label)**2)

#print('Coefficients: \n', lrModel.coef_)
print("Mean squared error: %.2f" % np.mean(( output - test_label) ** 2))
print('Variance score: %.2f' % lrModel.score(test_data, test_label))
# np.savetxt("output.csv", [test_label,output], delimiter=",")

