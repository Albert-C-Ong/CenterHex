#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

from hex import Hex

class Hexgrid:

    def __init__(self, radius):
        """
        Creates a circular hexgrid given a radius size
        """

        self.radius = radius
        self.rows = (2 * radius) + 1

        self.grid = []

        row_lengths = [x + self.radius for x in range(1, (self.rows - self.radius) + 1)] + \
                    [x for x in range(self.rows - 1, self.rows - self.radius - 1, -1)]

        for y, length in enumerate(row_lengths):
            self.grid.append([Hex(x, y) for x in range(length)])


    def __str__(self):

        output = ""

        for index, row in enumerate(self.grid, 1):
            offset = " " * abs(index - self.radius - 1)
            row_str = offset + "".join([str(item) + " " for item in row])

            output += row_str + "\n"

        return output


    def __iter__(self):
        for each in self.grid:
            yield 
    
          
    def __getitem__(self, indices):

        if not isinstance(indices, tuple):
            raise IndexError("Must have two indices")
        
        else:
            indices = tuple(indices)
            return self.grid[indices[1]][indices[0]]


#======================================================================================


if __name__ == "__main__":

    grid = Hexgrid(6)
    print(grid)

    print(grid[0, 0])
