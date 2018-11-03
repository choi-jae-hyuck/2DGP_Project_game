import game_framework
from pico2d import *
import random
import game_world

import main_state # map.값 확인후 제거

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
    def enter(hero, event):
        hero.vertical = 0
        hero.horizontal = 0
        if event == W_DOWN:
            hero.horizontal = 5
        elif event == A_DOWN:
            hero.vertical = -5
            hero.dir = False
        elif event == S_DOWN:
            hero.horizontal = -5
        elif event == D_DOWN:
            hero.vertical = 5
            hero.dir = True
        elif event == W_UP:
            hero.horizontal = 5
        elif event == A_UP:
            hero.vertical = -5
        elif event == S_UP:
            hero.horizontal = -5
        elif event == D_UP:
            hero.vertical = 5


    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if hero.timer>0 :
            hero.x+=hero.vertical
            hero.y += hero.horizontal
            hero.timer-=1

    @staticmethod
    def draw(hero):
        if hero.timer==0:
            if hero.dir == True:
                hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55, -3.141592, 'v', hero.drax,100+ hero.dray,40, 50)
            else :
                hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55, 180*-3.141592, ' ', hero.drax,100+ hero.dray,40, 50)
        else :
            if hero.dir == True:
                hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, -3.141592, 'v', hero.drax,100+hero.dray, 32, 50)
            else:
                hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, 180 * -3.141592, ' ',hero.drax,100+ hero.dray, 32, 50)


class RunState:

    @staticmethod
    def enter(hero, event):
        hero.vertical = 0
        hero.horizontal =0
        if event == W_DOWN:
            hero.horizontal = 5
        elif event == A_DOWN:
            hero.vertical = -5
            hero.dir = False
        elif event == S_DOWN:
            hero.horizontal = -5
        elif event == D_DOWN:
            hero.vertical = 5
            hero.dir =True
        elif event == W_UP:
            hero.horizontal = -5
        elif event == A_UP:
            hero.horizontal = 5
        elif event == S_UP:
            hero.vertical = 5
        elif event == D_UP:
            hero.vertical = -5
        hero.timer = 10

    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(hero):
        if hero.dir == True:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, -3.141592, 'v', hero.drax,100+ hero.dray,32, 50)
        else:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, 180*-3.141592 ,' ', hero.drax,100+ hero.dray,32,50)


next_state_table = {
    IdleState: {W_DOWN: RunState, A_DOWN: RunState, S_DOWN: RunState, D_DOWN: RunState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState},
    RunState: {W_DOWN: IdleState, A_DOWN: IdleState, S_DOWN: IdleState, D_DOWN: IdleState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState}
}

class HERO:
    def __init__(self):
        self.x, self.y= 525,125
        self.drax, self.dray=0,0
        self.state=0
        self.frame=0
        self.vertical = 0
        self.horizontal=0
        self.dir = True #true-right false-left
        self.timer=0
        self.image=load_image('hero.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def draw(self):
        self.cur_state.draw(self)
        print(main_state.tiles.dungeon.level[int(self.y//50)][int(self.x//50)])
        print(int(125//50))


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.x>425 and self.x<2625+1:
            self.drax=425
        elif self.x>2625:
            self.drax=self.x-2200;
        else :
            self.drax=self.x
        if self.y>325 and self.y<2075+1:
            self.dray=325
        elif self.y>2075 :
            self.dray=self.y-1750
        else :
            self.dray=self.y
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

class STAR:
    def __init__(self):
        self.x, self.y= 300,100
        self.state=0
        self.frame=0
        self.image=load_image('star.png')

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
