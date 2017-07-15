# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:14:59 2017

@author: maadland
"""
import random

def split_data(data, prob):
    """ splits data into fractions """
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results

def train_test_split(x, y, test_pct=.33):
    """ Splits training and test where x is the label and y are the features"""
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train) #(*zip) neat trick to unzip a file
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test

x = [0 if random.random() < 1 else 1 for x in range(1000)]
y = [(1, 0, 1) if random.random() < 1 else (0 ,0, 1) for x in range(1000)]
