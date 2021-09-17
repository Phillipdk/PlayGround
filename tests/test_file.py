# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:32:58 2021

@author: 1990phkj
"""

import os

def test_simple():
    assert True
    
def test_get_github_secrets():
    s = os.environ.get("SIMPLE")
    assert s == "Simple"