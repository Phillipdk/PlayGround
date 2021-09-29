# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:32:58 2021

@author: 1990phkj
"""

import os
import runpy

def test_simple():
    assert True
    
def test_get_github_secrets():
    s = os.environ.get("SIMPLE")
    assert s == "Simple"
    
def run_tutorial():
    runpy.run_path("C:\\Users\\1990phkj\\Documents\\IoT_Suite\\PlayGround\\Tutorial.py")
