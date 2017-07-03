# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 18:48:06 2017

@author: michael
"""

import queries
import datetime as dt
import pandas as pd

ledger = pd.DataFrame.from_dict(queries.get_ledger()['result']['ledger'],
                                orient='index').sort_values(by=['time'])
assets = list(set(ledger['asset']))