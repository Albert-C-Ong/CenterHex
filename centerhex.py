#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

from hexgrid import Hexgrid


class CenterHex:

    def __init__(self):

        self.rows = 11
        self.hexgrid = Hexgrid(self.rows)

        radius = self.hexgrid.radius
        self.hexgrid.grid[radius][radius].color = "center"


    def __str__(self):
        return str(self.hexgrid)


#======================================================================================


if __name__ == "__main__":
    game = CenterHex()
    print(game)


