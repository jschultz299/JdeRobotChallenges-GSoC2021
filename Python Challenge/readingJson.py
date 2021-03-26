#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:27:16 2019

@author: erivelton
"""

import json
import numpy as np
import random

with open('input.txt') as json_file:
    input = json.load(json_file)
    for mpt in input['main']:
        NLINS = mpt['NLINS']
        NCOLS = mpt['NCOLS']
    for pt in input['patterns']:
#        print(pt['name'],' : ')
        ptn = pt['pattern']
        numrows = len(ptn)
        numcols = len(ptn[0])
#        print(pt['place_auto'])
        X = np.zeros((NLINS, NCOLS))
        if pt['add'] == True:
            # Generate position
            ij = [random.randint(0,3), random.randint(0,3)]
            X[ij[0]:ij[0]+numrows,ij[1]:ij[1]+numcols] = pt['pattern']
            print(pt['name'])
            print(X)
