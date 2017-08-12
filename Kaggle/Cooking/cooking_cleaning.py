# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:28:39 2017

@author: maadland
"""
from nltk.stem import WordNetLemmatizer
LEMMATIZER = WordNetLemmatizer()
STOPWORDS = ["yellow", "purple", "green", "black",
             "purple", "white", "red", "chopped",
             "diced", "grated", "crushed", "small", "medium",
             "large", "low-fat", "fresh", "plain",
             "all-purpose", "extra-virgin", "nonfat", "dry", "reduced-fat",
             "minced", "plain", "crushed", "chopped", "whole", "brown",
             "boiling", "shredded", "grated", "pitted", "sliced", "heavy",
             "freshly", "yukon", "gold", "chunky", "low", "sodium", "dark",
             "part-skim", "frozen"]

def remove_stopwords(ingredient, stopwords):
    """ removes any words in the stopwords list
    """
    ingredient = ingredient.lower() # normalizes to lower case
    no_stops = [gram for gram in ingredient.split(" ") if gram not in stopwords]
    new_ingredient = " ".join(no_stops)
    return new_ingredient

def lemmatize_word(ingredient, lemmatizer):
    """ Lematizes and ingredient
    """
    ingredients = ingredient.split(" ")
    lemmas = [lemmatizer.lemmatize(x) for x in ingredients]
    return " ".join(lemmas)

def shorten_ingredient(ingredient):
    """ Shortens an ingredient to the core term
    """
    terms = set(["chicken", "flour", "milk", "rice", "pork",
                 "beef", "lettuce", "beans", "shrimp", "salt",
                 "cream"])
    # get just the overlapping terms in the set
    intersection = set(ingredient.split(" ")).intersection(terms)
    if intersection:
        return str(list(intersection)[0]) # casts the set to a list for indexing
    else:
        return ingredient

def remove_colors(ingredient):
    """ removes colors from an ingredient
    """
    colors = ["yellow", "purple", "green", "black",
              "purple", "white", "red"]
    no_colors = [gram for gram in ingredient.split(" ") if gram not in colors]
    colorless_string = " ".join(no_colors)
    return colorless_string

if __name__ == "__main__":
    ROW_1 = ["yellow onion", "gram masala", "black pepper"]
    ROW_2 = ["non-fat 2% milk", "chicken breasts", "all-purpose flour",
             "olive oil"]
    ROW_3 = ["cherry tomatoes", "red potatoes", "pitted olives"]
    ROW_1_NEW = [remove_stopwords(x, STOPWORDS) for x in ROW_1]
    ROW_2_NEW = [shorten_ingredient(x) for x in ROW_2]
    ROW_3_NEW = [lemmatize_word(x, LEMMATIZER) for x in ROW_3]
    