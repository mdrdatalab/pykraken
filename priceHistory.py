# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:05:15 2017

@author: michael
"""

import queries


def get_history(asset):
    #first check if price history has been saved, load it if so
    pairs = queries.get_pairs()
    pairs = list(pairs.keys())
    usd = asset+'ZUSD'
    if usd in pairs:
        
        