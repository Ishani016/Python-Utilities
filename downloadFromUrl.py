# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:49:54 2019

@author: Parashar
"""
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.holidify.com/images/bgImages/OOTY.jpg', preload_content=False)

with open('C:/Users/Parashar/Documents/ooty/result.jpg', 'wb') as out:
    while True:
        data = r.read(10)
        if not data:
            break
        out.write(data)

r.release_conn()