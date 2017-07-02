# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 06:19:39 2017

@author: michael
"""

import json
import urllib.request
import urllib.parse
import urllib.error

import time

import hashlib
import hmac
import base64

import connection


class API(object):
    
    def __init__(self, key='', secret='', conn=None):
        
        self.key = key
        self.secret = secret
        self.uri = 'https://api.kraken.com'
        self.apiversion = '0'
        self.conn = conn
        return
        
    def load_key(self, path):
        
        with open(path, 'r') as f:
            self.key = f.readline().strip()
            self.secret = f.readline().strip()
        return
        
    def set_connection(self, conn):
        
        self.conn = conn
        return
        
    def _query(self, urlpath, req, conn=None, headers=None):
        
        url = self.uri + urlpath
                
        if conn is None:
            if self.conn is None:
                conn = connection.Connection()
            else:
                conn = self.conn
                
        if headers is None:
            headers = {}
            
        ret = conn._request(url, req, headers)
        return json.loads(ret)
        
    def query_public(self, method, req=None, conn=None):
        
        urlpath = '/' + self.apiversion + '/public/' + method
        
        if req is None:
            req = {}
            
        return self._query(urlpath, req, conn)
        
    def query_private(self, method, req=None, conn=None):
        
        if req is None:
            req = {}
            
        # TODO: check if self.{key,secret} are set
        urlpath = '/' + self.apiversion + '/private/' + method
        
        req['nonce'] = int(1000*time.time())
        postdata = urllib.parse.urlencode(req)
        
        encoded = (str(req['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()
        
        signature = hmac.new(base64.b64decode(self.secret),
                             message, hashlib.sha512)
        sigdigest = base64.b64encode(signature.digest())
        
        headers = {
            'API-Key': self.key,        
            'API-Sign': sigdigest.decode()
        }

        return self._query(urlpath, req, conn, headers)

             
        
        
        
        
        