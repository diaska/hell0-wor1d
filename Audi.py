# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:07:31 2019

@author: Diana.Skakova
"""

# Python code to illustrate the Module 
class Audi: 
    # First we create a constructor for this class 
    # and add members to it, here models 
    def __init__(self): 
        self.models = ['q7', 'a6', 'a8', 'a3'] 
  
    # A normal print function 
    def outModels(self): 
        print('These are the available models for Audi') 
        for model in self.models: 
            print('\t%s ' % model) 