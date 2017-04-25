# Shala Chen
# accuracy = 0.788480088191
# variance = 1254753.11072

import sklearn
from sklearn import tree
import csv
import numpy as np
import scipy

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
dtModel = tree.DecisionTreeClassifier()
dtModel = dtModel.fit(train_data, train_label)

# Predict rts_likes using testing sets
output = dtModel.predict(test_data)
accuracy = sklearn.metrics.accuracy_score(test_label,output)
var = np.mean(abs(output - test_label)**2)

print 'accuracy =', accuracy
print 'variance =', var
# np.savetxt("output.csv", [test_label,output], delimiter=",")





