# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:51:10 2022

@author: hoson
"""

import pandas as pd

world=pd.read_csv('data/World Indicators.csv')
world=world.dropna()
world['Business Tax Rate']=world['Business Tax Rate'].str.rstrip("%").astype('float')/100
world['GDP'] = world['GDP'].str.replace(',', '')
world['GDP'] = world['GDP'].str.replace('$', '')
world['GDP']=world['GDP'].astype('float')
world['Health Exp/Capita']=world['GDP'].replace('$', '').astype('float')
world.to_csv('data/World Indicators-clean.csv')
