import game_framework
from pico2d import *
import random
import game_world

import main_state

class FISH:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=0
        self.frame=0
        self.image=load_image('enemy1.png')

    def draw(self):
        if(self.state==0):# idle
            self.image.clip_draw(self.frame * 34 +2,1485 * 1, 31, 31, self.x,100+ self.y)
        elif(self.state==1): #running
            self.image.clip_draw(self.frame * 34 +2,1451 * 1, 31, 31, self.x,100+ self.y)

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
