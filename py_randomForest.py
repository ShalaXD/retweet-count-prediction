# Shala Chen
# accuracy = 0.8737770428551743
# n = 18
# var = 1340817.8466997382

from sklearn.ensemble import RandomForestClassifier
import sklearn
import numpy as np
import matplotlib.pyplot as plt

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
# Iterate various number of estimators
accuracies = []
variances = []
for i in range(1,31):
    rfModel = RandomForestClassifier(n_estimators=i)
    rfModel.fit(train_data, train_label)
    output = rfModel.predict(test_data)
    
    accuracy = sklearn.metrics.accuracy_score(test_label,output)
    accuracies.append(accuracy) 
    var = np.mean(abs(output - test_label)**2)
    variances.append(var)

print 'accuracy =', max(accuracies)
print 'variance =', min(variances)

plt.plot(range(1,31), accuracies)
plt.xlabel('n_estimators')
plt.ylabel('accuracies')
plt.show()


