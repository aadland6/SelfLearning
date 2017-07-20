# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:10:54 2017

@author: maadland
"""
import pandas as pd
import numpy as np
import os 
# from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import neighbors 
from sklearn import ensemble
from sklearn import svm

def train_validate_test(df):
    """Breaks the data into training, test, and validation sets"""
    train, validate, test = np.split(df.sample(frac=1, random_state=42), 
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
    knn_report = classification_report(breaks["CVLabels"], knn_validate)
    print(knn_report)
    #### Random Forest Classifier ####
    rf_clf = ensemble.RandomForestClassifier(n_estimators=1000, # number of trees
                                             random_state=42)
    rf_clf.fit(breaks["TrainValues"], breaks["TrainLabels"])
    rf_validate = rf_clf.predict(breaks["CValues"])
    rf_report = classification_report(breaks["CVLabels"], rf_validate)
    print(rf_report)
    #### SVM Classifier ####
    # svm_clf = svm.SVC(decision_function_shape="ovo", random_state=42)
    # svm_clf.fit(breaks["TrainValues"], breaks["TrainLabels"])