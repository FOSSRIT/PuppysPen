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
import Constants

class PuppysPen:

    # Runs before the game loop begins
    def __init__(self, _py_screen):
        self.running = True # controls the exit of the game loop
        self.clock = pygame.time.Clock() # controls the frame rate
        self.forceAll = True # force an entire repaint of the screen on the next frame
        self.clicked = None # the ID of the object that was clicked
        self.py_screen = _py_screen

        self.grid_offset = self.center_coords(600, 400)
        self.grid_width = 200
        self.grid_height = 200
        self.num_rows = 5
        self.num_columns = 5
        self.row_height = self.grid_height / self.num_rows
        self.column_width = self.grid_width / self.num_columns
        
        self.mouse_grid_position = (0, 0)
        self.mouse_prev_grid_position = (0, 0)
        self.rect_origin = (0, 0)
        self.drawing_rect = False

        # grass green
        self.py_screen.fill((84,171,71))
        self.draw_grid(self.grid_offset[0], self.grid_offset[1], 600, 400, 6, 6)

    def center_coords(self, _w, _h):
        x_padding = int((Constants.WIDTH - _w) / 2.0)
        y_padding = int((Constants.HEIGHT - _h) / 2.0)
        print("center_coords", x_padding, y_padding)
        return (x_padding, y_padding)

    def draw_rectangle(self, _x, _y, _width, _height):
        pygame.draw.rect(self.py_screen, (255,255,255), (_x,_y,_width,_height), 1)

    def draw_grid(self, _x, _y, _width, _height, _num_rows, _num_columns):
        _row_height = int(_height / _num_rows)
        _column_width = int(_width / _num_columns)

        for i in range(0, _num_columns + 1):
            self.draw_rectangle(i * _column_width + _x, _y, 1, _height)

        for j in range(0, _num_rows + 1):
            self.draw_rectangle(_x, j * _row_height + _y, _width, 1)

    def begin_user_rectangle(self):
        self.drawing_rect = True
        self.rect_origin = self.mouse_grid_position

    def finish_user_rectangle(self):
        self.drawing_rect = False

        # Calculate perimeter and area of user-drawn rectangle
        # and compare it to the level criteria

    # Main game loop
    def run(self):
        self.main_screen = MainScreen(self.py_screen)
        self.play_screen = GameScreen(self.py_screen)

        # set the initial screen
        self.screen = self.main_screen

        # The main game loop.
        while self.running:

            # Pump GTK events
            while Gtk.events_pending():
                Gtk.main_iteration()
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    # Update mouse_grid_position based on current mouse position
                    pos = pygame.mouse.get_pos()
                    gridpos = (pos[0] - self.grid_offset[0]), pos[1] - self.grid_offset[1])
                    
                    if gridpos[0] <= 0 and gridpos[1] <= 0:
                        self.mouse_grid_position = (0, 0)
                    
                    elif gridpos[0] > 0 and gridpos[1] > 0:
                        grid_x = round(gridpos[0] / self.column_width)
                        grid_y = round(gridpos[1] / self.row_height)
                        self.mouse_grid_position = (grid_x, grid_y)
                    
                    elif gridpos[0] < 0:
                        grid_y = round(gridpos[1] / self.row_height)
                        self.mouse_grid_position = (0, grid_y)
                        
                    elif gridpos[1] < 0:
                        grid_x = round(gridpos[0] / self.column_width)
                        self.mouse_grip_position = (grid_x, 0)
                    
                    # TODO: Empty mousemove handler at the moment
                    self.screen.mousemove(pos)

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
                    if event.button == 1 or event.button == 3:
                        pos = pygame.mouse.get_pos()
                        self.clicked = self.screen.click(pos)

                        # TODO: throw this in click event handler, only for the
                        # GameScreen
                        if not self.drawing_rect:
                            # Start drawing rectangle
                            self.begin_user_rectangle()

                    else:
                        # Finish drawing rectangle
                        self.finish_user_rectangle()

                elif event.type == QUIT:
                    self.running = False

class Screen(object):
    def __init__(self):
        pass

    def click(self, pos):
        """ Default click event handler """
        print(pos)

    def mousemove(self, pos):
        """ Default mousemove event handler """
        print(pos)

class MainScreen(Screen):
    def __init__(self, _py_screen):
        super(MainScreen, self).__init__()
        self.py_screen = _py_screen

class GameScreen(Screen):
    def __init__(self, _py_screen):
        super(GameScreen, self).__init__()

# This function is called when the game is run directly from the command line:
# ./PuppysPen.py
def main():
    pygame.init()
    py_screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), \
            pygame.RESIZABLE) # 54 = height of sugar toolbar
    game = PuppysPen(py_screen)
    game.run()

if __name__ == '__main__':
    main()
