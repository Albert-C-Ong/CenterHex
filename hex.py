
#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.11
"""

class Hex:

    def __init__(self, color = None):

        self.color = color
        self.filled = self.color != None

    
    def __str__(self):

        color_to_str = {None : "_", 
                        "red" : "X", 
                        "black" : "O", 
                        "center" : " "}

        return color_to_str[self.color]