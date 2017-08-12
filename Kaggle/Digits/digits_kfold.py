# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:56:47 2017

@author: maadland
"""
import pandas as pd
import numpy as np
import os 
# from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import neighbors 
from sklearn import ensemble
from sklearn import linear_model


if __name__ == "__main__":
    cwd = os.getcwd()
    digits_frame = pd.read_csv("{0}/digits_train.csv".format(cwd))
   