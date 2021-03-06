# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:16:38 2017

@author: michael
"""


import api


k = api.API()
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
    
def get_trades(pair, since):
    '''
        Outputs: list of trades, last id for next
    '''
    req = {'pair':pair, 'since':since}
    return k.query_public('Trades', req)['result']
    


###Private
def get_balance():
    return k.query_private('Balance')['result']
    
def get_history():
    return k.query_private('TradesHistory')
    
def get_ledger():
    return k.query_private('Ledgers')['result']['ledger']