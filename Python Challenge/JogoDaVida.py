#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:05:44 2019

@author: erivelton
"""

from CelulaJogoDaVida import CelulaJogoDaVida
import numpy as np
import json
import random


# Extract seetings
with open('input.txt') as json_file:
    input = json.load(json_file)
    for pt in input['patterns']:
        print('here')
    for pt2 in input['main']:
        NLINS = pt2['NLINS']
    for pt3 in input['main']:
        NCOLS = pt2['NCOLS']

LOW_POP = 2
HIGH_POP = 3

class classException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class JogoDaVida:
    def __init__(self, nlins=NLINS, ncols=NCOLS, pop_low=LOW_POP,
                 pop_high=HIGH_POP):
        if nlins < 0:
            raise classException("Number of lines less than zero!")
        if ncols < 0:
            raise classException("Number of collumns less than zero!")

        self._nlins = nlins
        self._ncols = ncols
        self._game_board = []
        self._full_size = nlins * ncols
        self._pop_low = pop_low
        self._pop_high = pop_high

        # Initilize
        for i in range(0, self._full_size):
            self._game_board.append(CelulaJogoDaVida())

    @property
    def nlins(self):
        return self._nlins

    @nlins.setter
    def nlins(self, v):
        raise AttributeError

    @property
    def ncols(self):
        return self._ncols

    @ncols.setter
    def ncols(self, v):
        raise AttributeError

    @property
    def game_board(self):
        return self._game_board

    @game_board.setter
    def game_board(self, v):
        raise AttributeError

    @property
    def pop_low(self):
        return self._pop_low

    @pop_low.setter
    def pop_low(self, v):
        raise AttributeError

    @property
    def pop_high(self):
        return self._pop_high

    @pop_high.setter
    def pop_high(self, v):
        raise AttributeError

    def _par_coord_para_unidim(self, i, j):
        return i * self._ncols + j

    def _unidim_para_par_coord(self, coord):
        j = coord % self._ncols
        i = (coord - j) // self._ncols

        return i, j

    def show_board_game(self):
        for i in range(0, self._nlins):
            linha_impressao = ''
            for j in range(0, self._ncols):
                coord = self._par_coord_para_unidim(i, j)
                linha_impressao += \
                    self._game_board[coord].display_state_flag()
            print(linha_impressao)

        print('\n')

    def preenche_celulas_modular(self, modulo, espaco):
        mod_msg = "Valor de Modulo invalido. Deve ser maior do que zero."
        esp_msg = "Valor de Espaco invalido. Deve ser maior do que zero."

        if modulo < 0:
            raise classException(mod_msg)
        if espaco < 0:
            raise classException(esp_msg)

        m = modulo
        e = espaco

        with open('input.txt') as json_file:
            input = json.load(json_file)
            for mpt in input['main']:
                NLINS = mpt['NLINS']
                NCOLS = mpt['NCOLS']
                X = np.zeros((NLINS, NCOLS))
            for pt in input['patterns']:
                ptn = pt['pattern']
                numrows = len(ptn)
                numcols = len(ptn[0])
                if pt['add']:
                    if pt['place_auto']:
                        # Generate position
                        ij = [random.randint(0,3), random.randint(0,3)]
                        print(ij)
                        X[ij[0]:ij[0]+numrows,ij[1]:ij[1]+numcols] = pt['pattern']
                    else:
                        ij = pt['where']
                        X[ij[0]:ij[0]+numrows,ij[1]:ij[1]+numcols] = pt['pattern']

        ij = np.where(X== 1)
        print(ij)
        for i, j in zip(ij[0], ij[1]):
            coord = self._par_coord_para_unidim(i, j)
            self._game_board[coord].nasce()

    def _dentro_dos_limites(self, i, j):
        if i < 0 or j < 0:
            return False
        if i >= self._nlins or j >= self._ncols:
            return False

        return True

    def _conta_neighbors(self, posicao):
        x, y = self._unidim_para_par_coord(posicao)

        neighbors = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    novo_x = x + i
                    novo_y = y + j
                    if self._dentro_dos_limites(novo_x, novo_y):
                        pos_vizinho = \
                            self._par_coord_para_unidim(novo_x, novo_y)
                        if self._game_board[pos_vizinho].isItAlive():
                            neighbors += 1

        return neighbors

    def execute_one_step(self):
        lista_mudanca_estado = []

        for i in range(0, self._full_size):
            neighbors = self._conta_neighbors(i)

            if self._game_board[i].isItAlive():
                if (neighbors < self._pop_low) or (neighbors > self._pop_high):
                    lista_mudanca_estado.append(i)
            else:
                if neighbors == self._pop_high:
                    lista_mudanca_estado.append(i)

        for i in lista_mudanca_estado:
            self._game_board[i].change_state()
