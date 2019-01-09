# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 08:09:01 2019

@author: santhob
"""
import SynchronizedThread as st

if __name__ == "__main__": 
	for i in range(10): 
		st.main_task() 
		print("Iteration {0}: x = {1}".format(i,st.x)) 


        