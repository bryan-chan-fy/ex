# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:41:16 2022

@author: 
"""

# defining a decorator
def hello_decorator(func):
    
    def inner1():
        print("Hello, this is before function execution")
        
        # calling the actual function now
        # inside the wrapper function
        
        func()
        
        print("This is after function execution")
        
    return inner1

