
#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

class Hex:

    def __init__(self, x, y, color = None):

        self.color = color

        self.x = x
        self.y = y
        self.coord = (x, y)

    
    def __repr__(self):

        color_to_repr = {None : "_", 
                        "red" : "X", 
                        "black" : "O", 
                        "center" : " "}

        return color_to_repr[self.color]

    def filled(self):
        return self.color != None