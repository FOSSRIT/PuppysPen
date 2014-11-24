#!/usr/bin/python
'''
Primary pygame file. Deals with all the stuff.

Application structure taken from brendanwhitfield/planetary
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
    def __init__(self, _py_screen):
        self.running = True # controls the exit of the game loop
        self.clock = pygame.time.Clock() # controls the frame rate
        self.forceAll = True # force an entire repaint of the screen on the next frame
        self.clicked = None # the ID of the object that was clicked
        self.py_screen = _py_screen

        self.mouse_grid_position = (0, 0)
        self.mouse_prev_grid_position = (0, 0)
        self.rect_origin = (0, 0)
        self.drawing_rect = False

    def draw_rectangle(self, _x, _y, _width, _height):
        pass

    def draw_grid(self, _width, _height, _num_rows, _num_columns):
        _row_height = int(_height / _num_rows)
        _column_width = int(_width / _num_columns)

        for x in range(0, _num_columns + 1):
            draw_rectangle(x * _column_width, 0, 1, _height)

        for y in range(0, _num_rows + 1):
            draw_rectangle(0, y * _row_height, _width, 1)

    def begin_user_rectangle(self):
        self.drawing_rect = True
        self.rect_origin = mouse_grid_position
        
    def finish_user_rectangle(self):
        self.drawing_rect = False
        
        # Calculate perimeter and area of user-drawn rectangle
        # and compare it to the level criteria
    
    # Main game loop
    def run(self):
        self.main_screen = MainScreen()
        self.play_screen = GameScreen()

        # set the initial screen
        self.screen = self.main_screen

        # The main game loop.
        while self.running:

            # Pump GTK events
            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    # Update mouse_grid_position based on current mouse position
                    
                    # If mouse_grid position and mouse_prev_grid_position are different
                    if self.mouse_grid_position != self.mouse_prev_grid_position:
                        if not self.drawing_rect:
                            # Update the position of the yellow dot
                            pass

                        else:
                            # Update the position of the yellow rectangle
                            pass
                            
                        self.mouse_prev_grid_position = self.mouse_grid_position
                
                elif event.type == MOUSEBUTTONUP:
                    if not self.drawing_rect:
                        # Start drawing rectangle
                        self.begin_user_rectangle()
                    
                    else:
                        # Finish drawing rectangle
                        self.finish_user_rectangle()
                    
                elif event.type == QUIT:
                    self.running = False

                elif event.type == MOUSEBUTTONUP and \
                        (event.button == 1 or event.button == 3):
                    pos = pygame.mouse.get_pos()
                    self.clicked = self.screen.click(pos)

                elif event.type == MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.screen.mousemove(pos)

class Screen(object):
    def __init__(self):
        self.display = pygame.display
        self.window = pygame.display.get_surface()

    def click(self, pos):
        """ Default click event handler """
        print(pos)

    def mousemove(self, pos):
        """ Default mousemove event handler """
        print(pos)

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()

class GameScreen(Screen):
    def __init__(self):
        super(GameScreen, self).__init__()

# This function is called when the game is run directly from the command line:
# ./PuppysPen.py
def main():
    pygame.init()
    py_screen = pygame.display.set_mode((1200, 900 - 54), pygame.RESIZABLE) # 54 = height of sugar toolbar
    game = PuppysPen(py_screen)
    game.run()

if __name__ == '__main__':
    main()
