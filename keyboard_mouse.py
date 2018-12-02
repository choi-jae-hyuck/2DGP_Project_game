from pico2d import *

import main_state

class Mouse:
    def __init__(self):
        self.x, self.y = 0,0
        self.cursor=None
        self.fist=None
        self.select=False #false = cursor , True = fist
        if self.cursor is None:
            self.cursor=load_image('Resource\Mouse_cursor.png')
        if self.fist is None:
            self.fist=load_image('Resource\Fist_cursor.png')

    def update(self):
        self.x, self.y= main_state.mouse_x,main_state.mouse_y
        if main_state.hero.x-50<=self.x+main_state.tiles.scrollx*50<=main_state.hero.x+100 and main_state.hero.y - 50 <= self.y-100 + main_state.tiles.scrolly * 50 <= main_state.hero.y + 100:
            if main_state.number[int(self.y - 100 + main_state.tiles.scrolly * 50) // 50][int(self.x + main_state.tiles.scrollx * 50) // 50] is 2:
                self.select = True
            else:
                self.select = False
    def draw(self):
        if self.select is True:
            self.fist.clip_composite_draw(0, 0, 111, 112, 0, ' ', self.x + 10, self.y - 15, 30, 30)
        else:
            self.cursor.clip_composite_draw(0, 0, 462, 543, 1, ' ', self.x + 10, self.y - 15, 30, 30)


class Keyboard:
    def __init__(self):
        self.image=None
        if self.image is None:
            self.image=load_image('Resource\keyboard.png')

    def draw(self):
        self.image.clip_composite_draw(50, 99, 24, 26, 0, ' ', 415-30, 65, 30, 30)  # s
        self.image.clip_composite_draw(36, 70, 24, 26, 0, ' ', 380-30, 30, 30, 30) #a
        self.image.clip_composite_draw(64, 70, 24, 26, 0, ' ', 415-30, 30, 30, 30)  # s
        self.image.clip_composite_draw(92, 70, 24, 26, 0, ' ', 450-30, 30, 30, 30)  # d

    def update(self):
        pass