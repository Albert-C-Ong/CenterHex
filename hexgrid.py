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


    def diagonals(self, direction = 1):
        """
        Args:
            direction: default southeast, otherwise south west
        Returns:
            All of the diagonals in a hexgrid
        """

        radius = self.radius

        diags = []

        for index in range(radius * -1, radius + 1):

            diag = self.diagonal(index, direction)
            diags.append(diag)

        return diags
        

    def diagonal(self, index, direction = 1):
        """
        Args:
            index: starting index
            direction: default southeast, otherwise south west
        Returns:
            A diagonal of the hexgrid
        """

        radius = self.radius

        if direction == 1:
            # north-west + top edge
            edge_coords = [(0, x) for x in range(radius, 0, -1)] + \
                          [(x, 0) for x in range(radius + 1)]
        else:
            # top + north-east edge
            edge_coords = [(x, 0) for x in range(radius)] + \
                          [(x + radius, x) for x in range(radius + 1)]  
                      
        diag = []

        start_coord = edge_coords[index + 2]

        x = start_coord[0]
        y = start_coord[1]

        next_coord = self[x, y]

        while True:

            try:
                next_coord = self[x, y]
            except IndexError:
                break

            if direction == 1: 
                if y < radius:
                    transform = (1, 1)
                else:
                    transform = (0, 1)
            else:
                if y < radius:
                    transform = (0, 1)
                else:
                    transform = (-1, 1)

            diag.append(next_coord)

            x += transform[0]
            y += transform[1]

            if x < 0:
                break

        return diag


#======================================================================================


if __name__ == "__main__":

    grid = Hexgrid(2)

    diags = grid.diagonals(-1)

    for diag in diags:
        print([[hex.x, hex.y] for hex in diag])
