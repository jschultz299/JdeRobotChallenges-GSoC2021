#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:25:27 2019

@author: erivelton
"""

import json
 
input = {}  

input['main'] = [];
input['main'].append({
                'NLINS' : 10,
                'NCOLS' : 10,
                'N_STEPS' : 40
                })

input['patterns'] = []  

input['patterns'].append({ 
                'name': 'Glider',
                'pattern' : [[0, 0, 1],
                             [1, 0, 1],
                             [0, 1, 1]],
                'place_auto' : False,
                'add' : True,
                'where' : [0,0]
                })


#
############################### TEMPLATES ######################################
## http://conwaylife.com/wiki/Category:Patterns
#input['patterns'].append({ 
#                'name': 'r_pentomino',
#                'pattern' : [[0, 1, 1],
#                             [1, 1, 0],
#                             [0, 1, 0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'acorn',
#                'pattern' : [[0, 1, 0, 0, 0, 0, 0],
#                             [0, 0, 0, 1, 0, 0, 0],
#                             [1, 1, 0, 0, 1, 1, 1]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'spaceship',
#                'pattern' : [[0, 0, 1, 1, 0],
#                             [1, 1, 0, 1, 1],
#                             [1, 1, 1, 1, 0],
#                             [0, 1, 1, 0, 0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#
#input['patterns'].append({ 
#                'name': 'block_switch_engine',
#                'pattern' : [[0, 0, 0, 0, 0, 0, 1, 0],
#                             [0, 0, 0, 0, 1, 0, 1, 1],
#                             [0, 0, 0, 0, 1, 0, 1, 0],
#                             [0, 0, 0, 0, 1, 0, 0, 0],
#                             [0, 0, 1, 0, 0, 0, 0, 0],
#                             [1, 0, 1, 0, 0, 0, 0, 0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#
## WIKIPEDIA: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
## Still lifes
#input['patterns'].append({ 
#                'name': 'block',
#                'pattern' : [[1,1],
#                             [1,1]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'beehive',
#                'pattern' : [[0,1,1,0],
#                             [1,0,0,1],
#                             [0,1,1,0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'loaf',
#                'pattern' : [[0,1,1,0],
#                             [1,0,0,1],
#                             [0,1,0,1],
#                             [0,0,1,0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'tub',
#                'pattern' : [[0,1,0],
#                             [1,0,1],
#                             [0,1,0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
## Oscillators
#input['patterns'].append({ 
#                'name': 'blinker',
#                'pattern' : [[1,1,1]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'toad',
#                'pattern' : [[0,0,1,0],
#                             [1,0,0,1],
#                             [1,0,0,1],
#                             [0,1,0,0]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#input['patterns'].append({ 
#                'name': 'beacon',
#                'pattern' : [[1,1,0,0],
#                             [1,1,0,0],
#                             [0,0,1,1],
#                             [0,0,1,1]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })
#
#
## Spaceships
#input['patterns'].append({ 
#                'name': 'Glider',
#                'pattern' : [[0, 0, 1],
#                             [1, 0, 1],
#                             [0, 1, 1]],
#                'place_auto' : False,
#                'add' : False,
#                'where' : [0,0]
#                })


with open('input.txt', 'w') as outfile:  
    json.dump(input, outfile)
    
