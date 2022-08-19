# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:09:12 2022

@author: jbrownlow

First Assignment: find sum of first 100 
integers.
15 August 2022


"""

import numpy as np
list100 = np.linspace(1, 100, 100)
sum100 = sum(list100)
print('sum of first 100 integers is: {}'.format(sum100))

otherSum=0
for i in range(101):
    otherSum += i
    
print('otherSum = {}'.format(otherSum))





