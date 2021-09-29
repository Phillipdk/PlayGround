# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:38:20 2021

@author: 1990phkj
"""

import os
import runpy

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

runpy.run_path("Tutorial.py")
runpy.run_path("Tutorial_temp.py")

#os.remove("PrintStatement_out.py")