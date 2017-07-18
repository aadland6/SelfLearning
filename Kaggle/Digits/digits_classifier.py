# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:10:54 2017

@author: maadland
"""
import pandas as pd
import os 
from sklearn.model_selection import train_test_split
from sklearn import  metrics
from sklearn import neighbors 




if __name__ == "__main__":
    cwd = os.getcwd()
    full_train = pd.read_csv("{0}/digits_train.csv".format(cwd))
    labels = full_train["label"]
    values = full_train.drop("label", axis=1)
    labels_train, labels_test, values_train, values_test = train_test_split(
            labels, values, test_size = .2,random_state=42)
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=10,
                                             metric="euclidean")
    knn_clf.fit(values_train, labels_train)
    print("Predicting")
    knn_test = knn_clf.predict(values_test)
    knn_series = pd.Series(knn_test, index=labels_test.index)
    predicted_df = pd.DataFrame({"Actual":labels_test, "KNNPrediction":knn_test})
    predicted_df.to_csv("KNNPredictions.csv")