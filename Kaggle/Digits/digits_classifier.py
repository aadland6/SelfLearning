# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:10:54 2017

@author: maadland
"""
import pandas as pd
import numpy as np
import os 
from sklearn.model_selection import train_test_split
from sklearn import  metrics
from sklearn import neighbors 

def train_validate_test(df):
    """Breaks the data into training, test, and validation sets"""
    train, validate, test = np.split(df.sample(frac=1), 
                                     [int(.6*len(df)), int(.8*len(df))])
    train_labels = train["label"]
    train_values = train.drop("label", axis=1)
    validate_labels, test_labels = validate["label"], test["label"]
    validate_values = validate.drop("label", axis=1) 
    test_values = test.drop("label", axis=1)
    training_dict = {"TrainLabels":train_labels, "TrainValues":train_values,
                     "CVLabels":validate_labels, "CValues":validate_values,
                     "TestLabels":test_labels, "TestValues":test_values
                     }
    return training_dict


if __name__ == "__main__":
    cwd = os.getcwd()
    digits_frame = pd.read_csv("{0}/digits_train.csv".format(cwd))
    breaks = train_validate_test(digits_frame)
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=10,
                                             metric="euclidean")
    knn_clf.fit(breaks["TrainValues"], breaks["TrainLabels"])
    knn_validate = knn_clf.predict(breaks["CValues"])
#    train, validate, test = np.split(df.sample(frac=1), 
#                                     [int(.6*len(df)), int(.8*len(df))])
#    validate_labels, test_label = validate["label"], test["label"]
#    validate.drop("label", axis=1)
#    test.drop("label", axis=1)

#    labels = full_train["label"]
#    values = full_train.drop("label", axis=1)
#    labels_train, labels_test, values_train, values_test = train_test_split(
#            labels, values, test_size = .2,random_state=42)
#    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=10,
#                                             metric="euclidean")
#    knn_clf.fit(values_train, labels_train)
#    print("Predicting")
#    knn_test = knn_clf.predict(values_test)
#    knn_series = pd.Series(knn_test, index=labels_test.index)
#    predicted_df = pd.DataFrame({"Actual":labels_test, "KNNPrediction":knn_test})
#    predicted_df.to_csv("KNNPredictions.csv")