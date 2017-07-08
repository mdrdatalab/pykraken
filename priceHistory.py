# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:05:15 2017

@author: michael
"""

import queries
import time
import csv


def get_history(asset):
    #TODO: first check if price history has been saved, load it if so
    pairs = queries.get_pairs()
    pairs = list(pairs.keys())
    #I don't like only having it in USD anymore... fix this?
    usd = asset+'ZUSD'
    trades = []
    if usd in pairs:
        print('yes')
        last = 0
        temp = {usd: ['x'], last: 0}
        while temp[usd] != []:
            try:
                print(last)
                temp = queries.get_trades(usd, last)
                last = temp['last']
                trades.append(temp[usd])
                time.sleep(2)
            except Exception as e:
                pass
        
    return {'trades': trades, 'last': last}


a = time.time()
history = get_history('XETH')
print(time.time()- a)        

def hist_writer(pair, history):  
    with open('data\%s-history.csv' % pair, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow([history['last']])
        writer.writerows(history['trades'])

def hist_reader(pair):  
    trades = []  
    with open('data\%s-history.csv' % pair, 'r') as f:
        reader = csv.reader(f)
        #TODO: make sure last gets written properly, then fix below on read
        last = next(reader)[0]
        for row in reader:
            trades.append(row)
    history = {'last': last, 'trades': trades}
    return history
    