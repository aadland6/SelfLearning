# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:54:53 2017

@author: maadland
"""
import math
from collections import Counter

def euclidean_distance(p, q):
    """Calculates Euclidean distance between p and q in arbitrary dimensions"""
    pq_dims = zip(p, q)
    squared_values = [(x[0] - x[1])**2 for x in pq_dims]
    return math.sqrt(sum(squared_values))

def majority_vote(labels):
    """Gets the majority vote from a labeled training set"""
    vote_counts = Counter(labels)
    most_common, most_common_count = vote_counts.most_common(1)[0]
    num_most_common = len(most_common)
    if num_most_common == 1:
        return most_common
    else:
        return majority_vote(labels[:-1])

def toy_knn(k, labeled_points, new_point):
    """Toy KNN Classifier for a set of labeled points and a new one"""
    pass

p = [1, 2, 3, 4]
q = [2, 3, 4, 5]
print(euclidean_distance(p, q))

labels = ["apple", "peach", "peach", "cherry"]
b = majority_vote(labels)