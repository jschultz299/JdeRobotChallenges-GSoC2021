#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:05:44 2019

@author: erivelton
"""

class CelulaJogoDaVida:
    def __init__(self, life=False, life_flag='[X]', death_flag='[ ]'):
        # Indica se celula esta life
        self._life = life
        self._life_flag = life_flag
        self._death_flag = death_flag

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, v):
        raise AttributeError

    @property
    def life_flag(self):
        return self._life_flag

    @life_flag.setter
    def life_flag(self, v):
        raise AttributeError

    @property
    def death_flag(self):
        return self._death_flag

    @death_flag.setter
    def death_flag(self, v):
        raise AttributeError

    def display_state_flag(self):
        if self._life:
            return self._life_flag
        return self._death_flag

    def isItAlive(self):
        return self._life

    def change_state(self):
        self._life = not self._life

    # @brief    Give life to cell
    def nasce(self):
        self._life = True

    # @brief    Kill cell.
    def morre(self):
        self._life = False
