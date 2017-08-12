# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:28:39 2017

@author: maadland
"""

row_1 = ["yellow onion", "gram masala", "black pepper"]
def remove_colors(ingredient):
    """ removes colors from an ingredient
    """
    colors = ["yellow", "purple", "green", "black", 
              "purple", "white", "red"]
    no_colors = [gram for gram in ingredient.split(" ") if gram not in colors]
    colorless_string = " ".join(no_colors)
    return colorless_string

row_1_new = [remove_colors(x) for x in row_1]