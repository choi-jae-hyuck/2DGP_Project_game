from pico2d import *

import main_state

class Mouse:
    def __init__(self):
        self.x, self.y = 0,0
        self.cursor=None
        self.fist=None
        if self.cursor is None:
            self.cursor=load_image('Resource\Mouse_cursor.png')
        if self.fist is None:
            self.fist=load_image('Resource\Fist_cursor.png')

    def update(self):
        self.x, self.y= main_state.mouse_x,main_state.mouse_y
    def draw(self):
        self.cursor.clip_composite_draw(0, 0, 462, 543, 1, ' ', self.x + 10, self.y - 15, 30, 30)
        self.fist.clip_composite_draw(0, 0, 111, 112, 0, ' ', self.x + 10, self.y - 15, 30, 30)


class Keyboard:
    def __init__(self):
        self.image=None
        if self.image is None:
            self.image=load_image('Resource\keyboard.png')