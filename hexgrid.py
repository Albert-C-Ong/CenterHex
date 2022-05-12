#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

from hex import Hex

class Hexgrid:

    def __init__(self, rows):

        self.rows = rows
        self.radius = rows // 2

        self.grid = []

        row_lengths = [x + self.radius for x in range(1, (rows - self.radius) + 1)] + \
                    [x for x in range(rows - 1, rows - self.radius - 1, -1)]

        for length in row_lengths:
            self.grid.append([Hex() for x in range(length)])


    def __str__(self):

        output = ""

        for index, row in enumerate(self.grid, 1):
            offset = " " * abs(index - self.radius - 1)
            row_str = offset + "".join([str(item) + " " for item in row])

            output += row_str + "\n"

        return output


#======================================================================================


if __name__ == "__main__":
    grid = Hexgrid(11)
    print(grid)
