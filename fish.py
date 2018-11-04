import game_framework
from pico2d import *
import random
import game_world

import main_state

class Fish:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=1
        self.frame=0
        self.image=load_image('enemy1.png')

    def draw(self):
        if(self.state==0):# idle
            self.image.clip_draw(self.frame * 31+2 ,743, 31, 31, self.x,100+ self.y,50,50)
        if(self.state==1):# running
            self.image.clip_draw(self.frame * 35 ,668, 36, 38, self.x,100+ self.y,50,50)
        elif(self.state==2): #attack
            self.image.clip_draw(self.frame * 29+1,708 * 1, 29, 31, self.x,100+ self.y,50,50)

    def update(self):
        if(self.state==0):
            if(self.frame>4-1):
                self.frame=0
            self.frame=(self.frame+1)%4
        elif(self.state==1):
            self.frame=(self.frame+1)%3
        elif(self.state==2):
            self.frame=(self.frame+1)%5
