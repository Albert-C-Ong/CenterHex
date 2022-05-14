#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

from itertools import cycle
from hexgrid import Hexgrid


class CenterHex:

    def __init__(self):

        self.RADIUS = 5
        self.hexgrid = Hexgrid(self.RADIUS)

        self.hexgrid[self.RADIUS, self.RADIUS].color = "center"
        # self.grid = self.hexgrid.grid

        self.player_cycle = cycle(["Player 1", "Player 2"])
        self.current_player = next(self.player_cycle)


    def __str__(self):
        return str(self.hexgrid)


    def get_viable_coords(self):
        
        transforms = ((-1, -1), 
                      (0, -1),
                      (-1, 0),
                      (1, 0),
                      (-1, 1),
                      (1, 1))

        transforms_top_shift = ((-1, -1), 
                                (1, -1),
                                (-1, 0),
                                (1, 0),
                                (-1, 1),
                                (1, 1))

        transforms_bot_shift = ((-1, -1), 
                                (0, -1),
                                (-1, 0),
                                (1, 0),
                                (0, 1),
                                (1, 1))

        for y, row in enumerate(self.hexgrid):
            for hex in row:

                if y <= 4:
                    neighbor_transforms = transforms_bot_shift
                elif y >= 6:
                    neighbor_transforms = transforms_top_shift
                else:
                    neighbor_transforms = transforms

                # print(hex.coord)

                for x_trans, y_trans in neighbor_transforms:

                    neighbor_x = hex.x + x_trans
                    neighbor_y = hex.y + y_trans

                    # if neighbor_x >= 0 and neighbor_y >= 0:
                    #     print((neighbor_x, neighbor_y))

                    # print(neighbor)

                    try:
                        neighbor_hex = self.grid[neighbor_y][neighbor_x]
                    except IndexError:
                        continue

                    print(neighbor_hex.filled)
                print()


    def is_viable_coord(self, x, y):

        hex = self.hexgrid[x, y]

        if hex.filled():
            return False
        
        else:

            transforms = ((-1, -1), 
                        (0, -1),
                        (-1, 0),
                        (1, 0),
                        (-1, 1),
                        (1, 1))

            transforms_top_shift = ((0, -1), 
                                    (1, -1),
                                    (-1, 0),
                                    (1, 0),
                                    (-1, 1),
                                    (1, 1))

            transforms_bot_shift = ((-1, -1), 
                                    (0, -1),
                                    (-1, 0),
                                    (1, 0),
                                    (0, 1),
                                    (1, 1))
            if y <= 4:
                neighbor_transforms = transforms_bot_shift
            elif y >= 6:
                neighbor_transforms = transforms_top_shift
            else:
                neighbor_transforms = transforms

            
            neighbors_filled = []
                
            for x_trans, y_trans in neighbor_transforms:

                neighbor_x = hex.x + x_trans
                neighbor_y = hex.y + y_trans

                try:
                    neighbor_hex = self.hexgrid[neighbor_x, neighbor_y]
                except IndexError:
                    continue

                neighbors_filled.append(neighbor_hex.filled())

            return any(neighbors_filled)


    def play(self):

        print("Welcome to CenterHex!")
        print(self.hexgrid)
        print()

        while True:
            print(self.current_player + " turn:")
            x = int(input("x: ")) - 1
            y = int(input("y: ")) - 1

            if self.is_viable_coord(x, y):            

                if self.current_player == "Player 1":
                    new_color = "red"
                else:
                    new_color = "black"

                self.hexgrid[x, y].color = new_color

                print(self.hexgrid)

                self.current_player = next(self.player_cycle)

            else:
                print("Not a viable coordinate")
                continue

        



#======================================================================================


if __name__ == "__main__":
    game = CenterHex()
    game.play()


