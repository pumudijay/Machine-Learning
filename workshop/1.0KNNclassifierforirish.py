#loading the toy dataset from skykit learn
from sklearn.datasets import load_iris

#loading the dataset into variable iris
iris=load_iris()

#taking the features from dataset
data=iris.data

#taking the labels from dataset
target=iris.target

#train_test_spilt is a function to divide the dataset into training and testing
from sklearn.model_selection import train_test_split

#split data into ratio 10%
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

#KNeighborClassifier will load the KNN algorithm
from sklearn.neighbors import KNeighborsClassifier

#KNN algorithm is loaded to clsfr
clsfr=KNeighborsClassifier()

#train the module
clsfr.fit(train_data,train_target)

#testing model
predicted_results=clsfr.predict(test_data)

print("predicted_results",predicted_results)
print("test_target",test_target)
