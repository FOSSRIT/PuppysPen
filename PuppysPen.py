#!/usr/bin/python
'''
Primary pygame file. Deals with all the stuff.
'''

# python
import random

# gtk
from gi.repository import Gtk

# pygame
import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP, MOUSEMOTION, VIDEORESIZE, ACTIVEEVENT

# app

class PuppysPen:

    # Runs before the game loop begins
    def __init__(self, _screen):
        self.running = True
        self.screen = _screen;

    def draw_rectangle(self, _x, _y, _width, _height):
        pass

    def draw_grid(self, _width, _height, _num_rows, _num_columns):
        _row_height = int(_height / _num_rows)
        _column_width = int(_width / _num_columns)

        for x in range(0, _num_columns + 1):
            draw_rectangle(x * _column_width, 0, 1, _height)

        for y in range(0, _num_rows + 1):
            draw_rectangle(0, y * _row_height, _width, 1)

    # Main game loop
    def run(self):
        # The main game loop.
        while self.running:
            
            # Pump GTK events
            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

# This function is called when the game is run directly from the command line:
# ./PuppysPen.py
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 900 - 54), pygame.RESIZABLE) # 54 = height of sugar toolbar
    screen.fill((255,255,255))
    game = PuppysPen(screen)
    game.run()

if __name__ == '__main__':
    main()