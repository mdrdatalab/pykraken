# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 05:58:36 2017

@author: michael
"""

import http.client
import urllib.request
import urllib.parse
import urllib.error

class Connection(object):
    
    def __init__(self, uri='api.kraken.com', timeout=30):
        
        self.headers = {
            'User-Agent': 'pykraken'
        }
        self.conn = http.client.HTTPSConnection(uri, timeout=timeout)
        return
        
    def close(self):
        
        self.conn.close()
        return
        
    def _request(self, url, req=None, headers=None):
        
        if req is None:
            req = {}
            
        if headers is None:
            headers = {}
            
        data = urllib.parse.urlencode(req)
        headers.update(self.headers)
        
        self.conn.request('POST', url, data, headers)
        response = self.conn.getresponse()
        
        if response.status not in (200, 201, 202):
            raise http.client.HTTPException(response.status)
            
        return response.read().decode()
        
        
        
        