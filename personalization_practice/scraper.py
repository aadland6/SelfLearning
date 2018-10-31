#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:12:56 2018
"""
import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup 

def crawl_event(num):
    """Crawls an event based on the number 
    """
    link = "http://mtgtop8.com/event?e={0}".format(num)
    page_text = requests.get(link).text
    soup = BeautifulSoup(page_text)
    hrefs = [x for x in soup.find_all("a", href=True)]
    cleaned = [h["href"] for h in hrefs if "?e=" in h["href"]]
    return cleaned

def crawl_deck(deck_list):
    """Iterates through the deck list
    """
    bounty = None
    for deck in deck_list:
        try:
            deck_link = "http://mtgtop8.com/event{0}".format(deck)
            deck_text = requests.get(deck_link).text
            deck_soup = BeautifulSoup(deck_text)
            deck_hrefs = deck_soup.find_all("a", href=True)
            target = [x["href"] for x in deck_hrefs if "tcg_redir" in x["href"]]
            deckid = deck_link[deck_link.find("d=")+2:deck_link.find("&f=")]
            df = create_df(deck_link, target[0])
            csv_id = "decks/{0}.csv".format(deckid)
            df.to_csv(csv_id)
        except Exception as e:
            print(e)
            continue
    return bounty

def create_df(deck_link, target):
    """Creates a dataframe
    """
    card_count = []
    card_name = []
    deck_list = target.split("||")
    fmt = deck_link[-2:]
    deckid = deck_link[deck_link.find("d=")+2:deck_link.find("&f=")]
    for card in deck_list:
        try:
            count, name = card.split(" ", 1)
            card_count.append(count)
            card_name.append(name)
        except ValueError:
            continue
    out_df = pd.DataFrame()
    out_df["Name"] = card_name
    out_df["Count"] = card_count
    out_df["Format"] = fmt
    out_df["ID"] = deckid
    return out_df

if __name__ == "__main__":
    counter = 20415
    while counter > 100:
        print(counter)
        try:
            cleaned = crawl_event(counter)
            crawl_deck(cleaned )
        except Exception as e:
            print(e)
        counter -= 1
    