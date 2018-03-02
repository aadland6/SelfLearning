# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:52:03 2018

@author: maadland
"""

def beta_1(x_pred, y_values):
    """Coefficient Formula
    """
    xbar = sum(x_pred) / len(x_pred)
    ybar = sum(y_values) / len(y_values)
    numerator = sum([(xi - xbar) * (yi - ybar) for xi, yi in zip(x_pred, y_values)])
    denominator = sum([(xi - xbar) ** 2 for xi in x_pred])
    b1 = numerator / denominator
    return b1


def get_r2(actual, predicted):
    """gets the ssr
    """
    total = len(predicted)
    ybar = sum(actual) / total 
    # divergence from the mean
    ssto = sum([(xi - ybar)**2 for xi in predicted])
    # total variance from the regression line 
    sse = sum([(yi - xi)**2 for yi, xi in zip(actual, predicted)])
    # how much does a datapoint move from the mean 
    r2 = 1 - (sse / ssto)
    return r2

def gradient_descent(s_slope, s_intercept, l_rate, iter_val, x_train, y_train):
    """gradient descent function 
    """
    for i in range(iter_val):
        int_slope = 0 
        int_intercept = 0 
        # number of points
        n_pt = float(len(x_train))
        for i, xi in enumerate(x_train):
            # subtract because we're going down! 
            int_intercept = -(2/n_pt) * (y_train[i] - ((s_slope * xi) + s_intercept))
            int_slope = -(2/n_pt) * xi * (y_train[i] - ((s_slope * xi) + s_intercept))
        final_slope = s_slope - (l_rate * int_slope)
        final_intercept = s_intercept - (l_rate * int_intercept)
        s_slope = final_slope
        s_intercept = final_intercept
        # m is the slope 
        # b is the intercept 
    return s_slope, s_intercept


        
    return  s_slope, s_intercept

if __name__ == "__main__":
    x_train = [x for x in range(1, 101)]
    y_train = [x + .5 for x in range(1, 101)]
    learning_rate = .001
    start_slope = 0
    start_interscept = 0
    iteration = 100000
    grad_slope, grad_interscept = gradient_descent(start_slope, start_interscept, 
                                                   learning_rate, iteration, x_train, y_train)
    values = [xi * grad_slope + grad_interscept for xi in x_train]