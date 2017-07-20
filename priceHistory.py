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
    pair = asset+'ZUSD'
    
    #TODO: first check if price history has been saved, load it if so       
    if os.path.isfile('data\\'+pair+'-history.csv'):
        history = hist_reader(pair)
        last = history['last']
        trades = history['trades']
    #why list doesn't come out flat?
    if pair in pairs:
        print('yes')

        temp = {pair: ['x'], last: 0}
        while temp[pair] != []:
            try:
                print(last)
                temp = queries.get_trades(pair, last)
                last = temp['last']
                for t in temp[pair]:
                    trades.append(t)
                time.sleep(1)
            except Exception as e:
                print('Error: ', e)
    history = {'trades': trades, 'last': last}
    hist_writer(pair, history)    
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
    # get trade data
    # filter by window
    # break down into interval
    # iteratively retrieve ohlc per window
    pass
    
    



#asset or pair?
def groupHist(pair):
    #read history
    #for each trade, extract datetime
    #place in dict for year:month:date
    #return dict
    history = {}
    #maybe do this through get_history so it updates?
    trades = hist_reader(pair)['trades']
    for trade in trades:
        date = datetime.datetime.fromtimestamp(float(trade[2]))  #index of timestamp
        year = date.year
        month = date.month
        day = date.day
        if not year in history.keys():
            history[year] = {}
        if not month in history[year].keys():
            history[year][month] = {}
        if not day in history[year][month].keys():
            history[year][month][day] = []
        history[year][month][day].append(trade)
    print('Done')
    return history
            
        
    
    


