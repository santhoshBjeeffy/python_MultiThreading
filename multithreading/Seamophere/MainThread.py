# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 08:40:48 2019

@author: santhob
"""
import SemaphoreLockThread as slt

if __name__ == "__main__": 
    for i in range(10): 
        slt.main_task() 
        print("Iteration {0}: x = {1}".format(i,slt.x)) 