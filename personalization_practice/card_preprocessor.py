# -*- coding: utf-8 -*-
import json 
import pandas as pd 
import numpy as np 
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import math

STOPWORDS_STRING = ("a;the;of;to;this;it;that;or;and;if;with;on;" \
                    "its;as;from;for;an;gets;an;any;cant;be;is;" \
                    "then;in;when")

STOPWORDS = STOPWORDS_STRING.split(";")

def cosine(x, y):
    """Returns the cosine distance 
    """
    dot = sum([xi * yi for xi, yi in zip(x, y)])
    xi = sum([xi **2 for xi in x])
    yi = sum([yi **2 for yi in y])
    distance = 1 - (dot / (math.sqrt(xi) + math.sqrt(yi)))
    return distance

def clean_text(text):
    """Standardizes the texts and removes unwanted characters
    """
    text = text.lower()
    exclude_string = "[]{},.''â€”()!-/:;?¡¢©®²¶º»½âãïžˆ’€™"
    cleaned_string = "".join([x for x in text if x not in exclude_string])
    # replace some characters
    cleaned_string.replace("\n", "").replace("  ", " ")
    return cleaned_string 

def card_to_text(card):
    """Concatenates all the elements in a card to a single string 
    """
    full_string = ""
    for key, value in card.items():
        if key in ["layout", "imageName", "name"]:
            continue
        if key == "text":
            full_string = "{0} {1}".format(full_string, value)
        else:
            full_string = "{0} {1}_{2}".format(full_string, key, value)
    return full_string

def all_cards_to_text(cards):
    """Generates a list of cards and ignores duplicated names  
    """
    all_strings = []
    checked_names = []
    for key, value in card_dict.items():
        if key in checked_names:
            continue
        else:
            checked_names.append(key)
            current_string = card_to_text(value)
            all_strings.append(current_string)
    return all_strings, checked_names 

def tidy_cards(card_text):
    """Cleans and tokenizes the text of each card
    """
    text = clean_text(card_text)
    tokens = text.split()
    tokens = [x for x in tokens if x not in STOPWORDS]
    return tokens 

if __name__ == "__main__":
    with open("AllCards.json", "r") as f:
        card_json = json.load(f)
        card_dict = dict(card_json)
    card_strings, card_names = all_cards_to_text(card_dict)
    card_tokens = [tidy_cards(x) for x in card_strings]
    card_vectorizer = CountVectorizer(binary=True, lowercase=False, tokenizer=lambda x: x)
    card_vectorizer.fit(card_tokens)
    card_vector = card_vectorizer.transform(card_tokens)
    print(card_vector.shape)
    