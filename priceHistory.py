# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:05:15 2017

@author: michael
"""

import queries
import time
import csv
import os.path
import datetime
import numpy as np

def get_history(asset):
 
    pairs = queries.get_pairs()
    pairs = list(pairs.keys())
    last = 0    
    trades = []
    #TODO: I don't like only having it in USD anymore... fix this?
    usd = asset+'ZUSD'
    
    #TODO: first check if price history has been saved, load it if so       
    if os.path.isfile('data\\'+usd+'-history.csv'):
        history = hist_reader(usd)
        last = history['last']
        trades = history['trades']
    #why list doesn't come out flat?
    if usd in pairs:
        print('yes')

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
    history = {'trades': trades, 'last': last}
    hist_writer(usd, history)    
    return history
    

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



def compute_ohlc(trades):
    '''
    takes a window of trades and computes open price, close price, low price,
    high price, volume weighted average price, volume, and count
    '''
    trades = np.array(trades)[:,0:3].astype(float)
    count = len(trades)
    p_open = trades[0][0]
    p_close = trades[-1][0]    
    p_high = max(trades[:,0])
    p_low = min(trades[:,0])
    volume = sum(trades[:,1])
    vwap = sum(trades[:,0]*trades[:,1])/volume
    ohlc = {'open': p_open,
            'close': p_close,
            'high': p_high,
            'low': p_low,
            'volume': volume,
            'vwap': vwap,
            'count': count}
            
    return ohlc
   
    
def get_ohlc(pair, interval=1440, start=None, end=None):
    '''
    retrieves trade history for a pair between start and end
    and returns ohlc data for that window at specified interval
    '''
    pass
    
    
