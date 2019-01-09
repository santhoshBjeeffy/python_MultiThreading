# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 08:19:50 2019

@author: santhob
"""
import MultiThreadExample as mt
import threading

if __name__=='__main__':
    #creating thread
    thread1 = threading.Thread(target=mt.Square,args=(10,))
    thread2 = threading.Thread(target=mt.Cube,args=(12,))
    
    
    #Starting thread
    thread1.start()
    thread2.start()
    
    # wait untill thread1 is completed
    thread1.join()
    #wait untill thread2 is completed
    thread2.join()
    
    #both threads completed
    print("done")

