# Shala Chen
# Shala Chen
# accuracy = 0.87046989114
# variance = 1326306.18327

from sklearn.neural_network import MLPClassifier
import sklearn
import numpy as np

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
nnModel = MLPClassifier(alpha=1e-5, hidden_layer_sizes=(10,10,10))
nnModel.fit(train_data, train_label)

# Predict rts_likes using testing sets
output = nnModel.predict(test_data)
accuracy = sklearn.metrics.accuracy_score(test_label,output)
var = np.mean(abs(output - test_label)**2)

print 'accuracy =', accuracy
print 'variance =', var
