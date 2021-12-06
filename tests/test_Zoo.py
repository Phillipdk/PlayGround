# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:47:47 2021

@author: 1990phkj
"""

import pytest

from Zoo import Lion

# First Sprint
def test_Lion():
    assert Lion()
    
def test_Lion_age():
    assert Lion(3)
    
def test_Lion_negative_age():
    with pytest.raises(AssertionError):
        assert Lion(-2)
        
        
# Second Sprint
