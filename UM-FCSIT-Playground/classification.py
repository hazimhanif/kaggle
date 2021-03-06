from sklearn.tree import DecisionTreeClassifier
import pandas as pd

training = pd.read_csv(open("C:/Users/Hazim/Downloads/training_set.csv"))

training_data = training.ix[:,0:2]
training_target = training.ix[:,3]

model = DecisionTreeClassifier()
model.fit(training_data, training_target)

# make predictions
expected = training_target
predicted = model.predict(training_data)
   
# summarize the fit of the model
print("\nThe model info : \n")
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

# display the accuracy of the model classification/prediction using training set
print("The accuracy: ")
print(metrics.accuracy_score(expected,predicted))




