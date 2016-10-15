# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:32:53 2016

@author: laura
"""

consecutive=0
n=1

Can=[6, 9, 20]
Cant=[0]

while (consecutive<6):
    found=0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m = i*6 + j*9+ k*20
                if (m==n):
                    found=1             
    if(found==1):
        consecutive=consecutive+1
    else:
        consecutive=0
        Cant.append(n)
    n+=1
        
print ('The highest number of nuggets that you CANNOT get is', max(Cant), )
