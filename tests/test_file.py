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
    
def test_run_tutorial_temp():
    #input file
    fin = open("Tutorial.py", "rt")
    #output file to write the result to
    fout = open("Tutorial_temp.py", "wt")
    #for each line in the input file
    for line in fin:
    	#read replace the string and write to output file
    	fout.write(line.replace('base_url = "https://edrmedesoapiservice.azurewebsites.net/"' , 'base_url = "https://edrmedesoapiservice-development.azurewebsites.net/"'))
    #close input and output files
    fin.close()
    fout.close()
    
    runpy.run_path("Tutorial_temp.py")
    os.remove("Tutorial_temp.py")

#def test_run_tutorial():
#    runpy.run_path("Tutorial.py")
