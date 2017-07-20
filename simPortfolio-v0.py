# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:32:51 2017

@author: michael
"""

import queries

#TODO make this work for all pairs...
#works for XXBT, XETH

#TODO make one for historical prices...

class portfolio():
    
    def __init__(self, initial_funds):
        self.initial_funds = initial_funds
        self.balance = {'ZUSD': self.initial_funds}
    


    def buy(self, asset, qty):
        price = get_price('buy', asset)
        #check available funds
        cost = price * qty
        if self.balance['ZUSD'] >= cost:
            self.balance['ZUSD'] -= cost
            if not asset in self.balance.keys():
                self.balance[asset] = 0
            self.balance[asset] += qty
        else:
            print('Insufficient Funds')
        
    def sell(self, asset, qty):
        if not asset in self.balance.keys():
            print('Insusfficient Funds')
            return
        if self.balance[asset] < qty:
            print('Insufficient Funds')
            return
        price = get_price('sell', asset)
        self.balance['ZUSD'] += price*qty
        self.balance[asset] -= qty
        
    

def get_price(action, asset):
    pair = asset +'ZUSD'
    orders = queries.get_orders(pair)[pair]
    if action == 'buy':
        prices = orders['asks']
    else:
        prices = orders['bids']
    #simple version here takes price as first element
    #TODO incorporate qty
        
    return float(prices[0][0])


