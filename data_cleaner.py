# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:51:10 2022

@author: hoson
"""

import pandas as pd
import numpy as np
world=pd.read_csv('data/World Indicators.csv')

world['Business Tax Rate']=world['Business Tax Rate'].str.rstrip("%").astype('float')/100
world['GDP'] = world['GDP'].str.replace(',', '')
world['GDP'] = world['GDP'].str.replace('$', '')
world['GDP']=world['GDP'].astype('float')
world['Health Exp/Capita']=world['GDP'].replace('$', '').astype('float')
for i in range(len(world.columns.values)-2):
    world[world.columns.values[i]]=world[world.columns.values[i]].replace(np.NaN,world[world.columns.values[i]].mean())
print(world.isnull().sum())    
world.to_csv('data/World Indicators-clean.csv')

