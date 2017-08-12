# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:28:39 2017

@author: maadland
"""
stopwords = ["yellow", "purple", "green", "black", 
             "purple", "white", "red", "chopped", 
             "diced", "grated", "crushed", "small", "medium",
             "large", "low-fat", "fresh", "plain", 
             "all-purpose", "extra-virgin", "nonfat", "dry","reduced-fat", 
             "minced", "plain", "crushed", "chopped", "whole", "brown",
             "boiling", "shredded", "grated", "pitted", "sliced", "heavy", 
             "freshly", "yukon", "gold", "chunky", "low", "sodium", "dark",
             "part-skim", "frozen"]

def remove_stopwords(ingredient, stopwords):
    """ removes any words in the stopwords list
    """
    no_stops = [gram for gram in ingredient.split(" ") if gram not in stopwords]
    new_ingredient = " ".join(no_stops)
    return new_ingredient

def remove_colors(ingredient):
    """ removes colors from an ingredient
    """
    colors = ["yellow", "purple", "green", "black", 
              "purple", "white", "red"]
    no_colors = [gram for gram in ingredient.split(" ") if gram not in colors]
    colorless_string = " ".join(no_colors)
    return colorless_string

def shorten_ingredient(ingredient):
    """ shortens an ingredient to the core term
    """
    terms = set(["chicken", "flour", "milk", "rice", "pork", 
                 "beef", "lettuce", "beans", "shrimp", "salt"])
    # get just the overlapping terms in the set
    intersection = set(ingredient.split(" ")).intersection(terms)
    if intersection:
        return str(list(intersection)[0]) # casts the set to a list for indexing
    else:
        return ingredient


if __name__ == "__main__":
    row_1 = ["yellow onion", "gram masala", "black pepper"]
    row_2 = ["non-fat 2% milk", "chicken breasts", "all-purpose flour",
         "olive oil"]
    row_1_new = [remove_stopwords(x, stopwords) for x in row_1]
    row_2_new = [shorten_ingredient(x) for x in row_2]
    