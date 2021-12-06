# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:46:36 2021

@author: 1990phkj
"""

class Lion:
    def __init__(self, age=0):
        if age < 0:
            raise AssertionError
        else:
            self.age = age
        
    
