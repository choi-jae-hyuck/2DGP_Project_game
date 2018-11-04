import game_framework
from pico2d import *
import random
import game_world

import main_state

W_DOWN, A_DOWN, S_DOWN, D_DOWN,W_UP, A_UP, S_UP, D_UP = range(8)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): W_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYUP, SDLK_w): W_UP,
    (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYUP, SDLK_s): S_UP,
    (SDL_KEYUP, SDLK_d): D_UP
}
class IdleState:

    @staticmethod
    def enter(fish, event):
        pass


    @staticmethod
    def exit(fish, event):
        if event == None:
            pass

    @staticmethod
    def do(fish):
        fish.frame = (fish.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if fish.timer > 0:
            if fish.move==0:
                fish.x +=5
            elif fish.move ==1:
                fish.x -=5
            elif fish.move ==2:
                fish.y -=5
            elif fish.move ==3:
                fish.y +=5
            fish.timer -= 1

    @staticmethod
    def draw(fish):
        if fish.dir == True:
            fish.image.clip_composite_draw(int(fish.frame) * 31 + 2, 743, 31, 31, -3.141592, 'v', fish.x,100 + fish.y, 50, 50)
        else :
            fish.image.clip_composite_draw(int(fish.frame) * 31 + 2, 743, 31, 31,180*-3.141592, ' ', fish.x, 100 + fish.y, 50, 50)


class RunState:

    @staticmethod
    def enter(fish, event):
        fish.timer=10

    @staticmethod
    def exit(fish, event):
        if event == None:
            pass

    @staticmethod
    def do(fish):
        fish.frame = (fish.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(fish):
        if fish.dir == True:
            fish.image.clip_composite_draw(int(fish.frame) * 35, 668, 36, 38,-3.141592, 'v', fish.x, 100 + fish.y, 50,50)
        else:
            fish.image.clip_composite_draw(int(fish.frame) * 35, 668, 36, 38, 180*-3.141592 ,' ', fish.x, 100 + fish.y, 50, 50)

next_state_table = {
    IdleState: {W_DOWN: RunState, A_DOWN: RunState, S_DOWN: RunState, D_DOWN: RunState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState},
    RunState: {W_DOWN: IdleState, A_DOWN: IdleState, S_DOWN: IdleState, D_DOWN: IdleState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState}
}


class Fish:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=1
        self.frame=0
        self.timer=0
        self.image=load_image('enemy1.png')
        self.dir=True
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    #def draw(self):
        #if(self.state==0):# idle
            #self.image.clip_draw(self.frame * 31+2 ,743, 31, 31, self.x,100+ self.y,50,50)
        #if(self.state==1):# running
            #self.image.clip_draw(self.frame * 35 ,668, 36, 38, self.x,100+ self.y,50,50)
        #elif(self.state==2): #attack
            #self.image.clip_draw(self.frame * 29+1,708 * 1, 29, 31, self.x,100+ self.y,50,50)

    def draw(self):
        self.cur_state.draw(self)

    #def update(self):
        #if(self.state==0):
            #if(self.frame>4-1):
                #self.frame=0
            #self.frame=(self.frame+1)%4
        #elif(self.state==1):
            #self.frame=(self.frame+1)%3
        #elif(self.state==2):
            #self.frame=(self.frame+1)%5

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def add_event(self, event):
        self.event_que.insert(0, event)