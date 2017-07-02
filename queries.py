# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:16:38 2017

@author: michael
"""


import API


k = API.API()
k.load_key('kraken.key')

###Public
def get_pairs():
    '''Returns pairs'''

    pairs = k.query_public('AssetPairs')
    # TODO: error handling
    # TODO: clean up returned data  
    
    return pairs['result']
    
def get_ticker(assetPairs):
    '''
        Input: comma delimited list of asset pairs
        Output:
    '''
    # TODO: error handling
    req  = {'pair':','.join(assetPairs)}
    ticker = k.query_public('Ticker', req)
    return ticker['result']

def get_orders(pair):

    req = {'pair':pair}
    ob = k.query_public('Depth', req)
    return ob['result']


###Private
def get_balance():
    return k.query_private('Balance')
    
def get_history():
    return k.query_private('TradesHistory')