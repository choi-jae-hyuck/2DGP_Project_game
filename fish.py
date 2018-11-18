import game_framework
from pico2d import *
import random
import game_world

import main_state

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Fish:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=0
        self.frame=0
        self.timer=0
        self.image=load_image('Resource\character\enemy1.png')
        self.dir=False

    def draw(self):
        if(self.dir==True):
            if(self.state==0):# idle
                self.image.clip_composite_draw(int(self.frame) * 31 + 2, 743, 31, 31, -3.141592, 'v', self.x, 100 + self.y,50, 50)
            if(self.state==1):# running
                self.image.clip_composite_draw(int(self.frame) * 35 ,668, 36, 38, -3.141592, 'v', self.x,100+ self.y,50,50)
            elif(self.state==2): #attack
                self.image.clip_composite_draw(int(self.frame) * 29+1,708 * 1, 29, 31, -3.141592, 'v', self.x,100+ self.y,50,50)
        elif (self.dir == False):
            if (self.state == 0):  # idle
                self.image.clip_composite_draw(int(self.frame) * 31 + 2, 743, 31, 31, 180 * -3.141592, ' ', self.x,100 + self.y, 50, 50)
            if (self.state == 1):  # running
                self.image.clip_composite_draw(int(self.frame) * 35, 668, 36, 38, 180 * -3.141592, ' ', self.x, 100 + self.y, 50, 50)
            elif (self.state == 2):  # attack
                self.image.clip_composite_draw(int(self.frame) * 29 + 1, 708 * 1, 29, 31, 180 * -3.141592, ' ', self.x,100 + self.y, 50, 50)


    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if(self.state==0):
            self.frame=(self.frame)%4
        elif(self.state==1):
            self.frame=(self.frame)%3
        elif(self.state==2):
            self.frame=(self.frame)%5

        if game_framework.turn==False:
            pass


    def handle_event(self, event):
       pass

    def add_event(self, event):
      pass