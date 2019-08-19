# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:06:32 2019

@author: Diana.Skakova
"""

# Python code to illustrate the Modules 
class Bmw: 
    # First we create a constructor for this class 
    # and add members to it, here models 
    def __init__(self): 
        self.models = ['i8', 'x1', 'x5', 'x6'] 
   
    # A normal print function 
    def outModels(self): 
        print('These are the available models for BMW') 
        for model in self.models: 
            print('\t%s ' % model) 