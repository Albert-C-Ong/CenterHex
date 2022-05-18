#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
Written by Albert Ong

Created: 2022.05.17
"""

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window


Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
# Window.clearcolor = (1.0, 1.0, 1.0, 1)

# Window.size = (1280, 720)


class CenterHexApp(App):

    def __init__(self):
        super().__init__()
        self.RADIUS = 5
        self.ROWS = self.RADIUS * 2 + 1
        self.title = "CenterHex"


    def row_lengths(self, radius):

        rows = self.ROWS

        row_lengths = [x + radius for x in range(1, (rows - radius) + 1)] + \
                        [x for x in range(rows - 1, rows - radius - 1, -1)]

        row_lengths_dict = {}

        for key, value in enumerate(row_lengths):
            row_lengths_dict[key] = value



    def build(self):
        root_layout = BoxLayout()
        root_layout.orientation = "vertical"

        row_lengths = [x + self.RADIUS for x in range(1, (self.ROWS - self.RADIUS) + 1)] + \
                      [x for x in range(self.ROWS - 1, self.ROWS - self.RADIUS - 1, -1)]

        for y, length in enumerate(row_lengths):
            
            row = BoxLayout()
            row.orientation = "horizontal"
            row.minimum_width = 50 * length

            for x in range(length):
                button_text = str(x) + ", " + str(y)
                row.add_widget(Button(text = button_text, size = ("10", "10")))

            root_layout.add_widget(row)

        return root_layout


if __name__ == '__main__':
    CenterHexApp().run()