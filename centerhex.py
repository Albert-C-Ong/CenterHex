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

        self.player_cycle = cycle(["Player 1", "Player 2"])
        self.current_player = next(self.player_cycle)


    def __str__(self):
        return str(self.hexgrid)


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


    def check_win(self):

        rows = self.hexgrid.grid

        diagonals = self.hexgrid.diagonals() + self.hexgrid.diagonals(-1)

        for column in rows + diagonals:
            for index in range(len(column) - 4):
                win = column[index : index + 5]

                if all([hex.color == "red" for hex in win]):
                    return True
                elif all([hex.color == "black" for hex in win]):
                    return True

        return False


    def play(self):

        print("Welcome to CenterHex!")
        print(self.hexgrid)
        print()

        while True:
            print(self.current_player + " turn:")

            inputs = (input("x, y: ")).split(", ")
            x = int(inputs[0]) - 1
            y = int(inputs[1]) - 1

            if self.is_viable_coord(x, y):            

                if self.current_player == "Player 1":
                    new_color = "red"
                else:
                    new_color = "black"
                    
                self.hexgrid[x, y].color = new_color
                print(self.hexgrid)


                if self.check_win():
                    print(self.current_player + " wins!")
                    break


                self.current_player = next(self.player_cycle)

            else:
                print("Not a viable coordinate\n")
                continue

        



#======================================================================================


if __name__ == "__main__":
    game = CenterHex()
    game.play()
