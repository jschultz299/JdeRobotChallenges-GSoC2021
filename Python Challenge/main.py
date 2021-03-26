# _*_ coding: utf-8 _*_

"""
Created on Tue Apr  2 00:05:44 2019

@author: erivelton
"""

from JogoDaVida import JogoDaVida
import time

import json
import numpy as np
import random
import os
import sys

import json


with open('input.txt') as json_file:
    input = json.load(json_file)
    for pt in input['main']:
        N_STEPS = pt['N_STEPS']

def main():
    jdv = JogoDaVida()
    jdv.preenche_celulas_modular(modulo=3, espaco=5)
    jdv.show_board_game()

    for i in range(0, N_STEPS):
        jdv.execute_one_step()
        os.system('clear')
        jdv.show_board_game()
        time.sleep(.1)

if __name__ == '__main__':
    main()
