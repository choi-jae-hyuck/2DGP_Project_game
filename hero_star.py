from pico2d import *
import random

W_DOWN, A_DOWN, S_DOWN, D_DOWN,W_UP, A_UP, S_UP, D_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): W_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYUP, SDLK_w): W_DOWN,
    (SDL_KEYUP, SDLK_a): A_DOWN,
    (SDL_KEYUP, SDLK_s): S_DOWN,
    (SDL_KEYUP, SDLK_d): D_DOWN
}

class HERO:
    def __init__(self):
        self.x, self.y= 100,100
        self.state=0
        self.frame=0
        self.image=load_image('hero.png')

    def draw(self):
        if(self.state==0): #idle
            self.image.clip_draw(self.frame * 41 +1,1140 * 1, 40, 55, self.x, self.y)
        elif(self.state==1): #running
            self.image.clip_draw(self.frame * 33 +1,1081 * 1, 32, 57, self.x, self.y)

    def update(self):
        if(self.state==0 or self.state==1):
            self.frame=(self.frame+1)%6
        elif(self.state==3):
            if(self.frame>6-1):
                self.frame=0
                
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

class STAR:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=0
        self.frame=0
        self.image=load_image('star.png')

    def draw(self):
        if(self.state==0):# idle
            self.image.clip_draw(self.frame * 34 +2,1485 * 1, 31, 31, self.x, self.y)
        elif(self.state==1): #running
            self.image.clip_draw(self.frame * 34 +2,1451 * 1, 31, 31, self.x, self.y)

    def update(self):
        if(self.state==0):
            if(self.frame>4-1):
                self.frame=0
            self.frame=(self.frame+1)%4
        elif(self.state==1):
            self.frame=(self.frame+1)%8
        elif(self.state==3):
            if(self.frame>11-1):
                self.frame=0
