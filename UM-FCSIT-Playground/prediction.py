from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

training = pd.read_csv(open("C:/Users/Hazim/Downloads/training_set.csv"))
testing = pd.read_csv(open("C:/Users/Hazim/Downloads/test_set.csv"))

training_data = training.ix[:,0:2]
training_target = training.ix[:,3]

testing_data = testing.ix[:,0:2]

model = DecisionTreeClassifier()
model.fit(training_data, training_target)

# make predictions
predicted = model.predict(testing_data)

# creating dataframe for id and predicted values
id = pd.DataFrame(list(range(1, len(predicted) + 1)),columns=['Id'])
predicted = pd.DataFrame(predicted,columns=['Prediction'])

# combining id and predicted dataframe
output = pd.concat([id, predicted], axis=1)

# ouput to a csv file
pd.DataFrame(output).to_csv('D:/prediction.csv',index=False)


