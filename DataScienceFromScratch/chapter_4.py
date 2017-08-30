# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:53:07 2017

@author: maadland
"""
def vector_addition(v1, v2):
    """ Adds two vectors together
    """
    vector_sum = [v1_i + v2_i for v1_i, v2_i in zip(v1, v2)]
    return vector_sum

def vector_subtraction(v1, v2):
    """ Subtracts two vectors together
    """
    vector_sum = [v1_i - v2_i for v1_i, v2_i in zip(v1, v2)]
    return vector_sum

def vector_total(vectors):
    """ Adds all the vectors together
    """
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_addition(result, vector)
    return result

def dot_product(v1, v2):
    """ Computes the sum of componentwise products 
    """
    component_products = [v1_i * v2_i for v1_i, v2_i in zip(v1, v2)]
    dot = sum(component_products)
    return dot

if __name__ == "__main__":
    # age, height, weight
    ryan = [30, 5.10, 160]
    tom = [22, 6.2, 175]
    ian = [26, 5.11, 155]
    people = [ryan, tom, ian]
    vector_addition(ryan, tom)
    all_people = vector_total(people)
    print(dot_product(ryan, ian))
    
    