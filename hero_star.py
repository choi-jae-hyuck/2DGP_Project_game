import game_framework
from pico2d import *
import random
import game_world

import main_state # map.값 확인후 제거

W_DOWN, A_DOWN, S_DOWN, D_DOWN,W_UP, A_UP, S_UP, D_UP,Left_Click= range(9)

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
    (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT): Left_Click
}
class IdleState:

    @staticmethod
    def enter(hero, event):
        hero.vertical = 0
        hero.horizontal = 0


    @staticmethod
    def exit(hero, event):
        if event == None :
            pass


    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(hero):
        if hero.timer==0:
            if hero.dir == True:
                hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55,-3.141592, 'v',hero.drax + 25, 100 + hero.dray + 25, 40, 50)
            else :
                hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55, 180*-3.141592, ' ', hero.drax+25,100+ hero.dray+25,40, 50)
        else :
            if hero.dir == True:
                hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, -3.141592, 'v', hero.drax+25,100+hero.dray+25, 32, 50)
            else:
                hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, 180 * -3.141592, ' ',hero.drax+25,100+ hero.dray+25, 32, 50)

class RunState:

    @staticmethod
    def enter(hero, event):
        hero.vertical = 0
        hero.horizontal =0
        if event == W_DOWN:
            if main_state.number[int(hero.y//50)+1][int(hero.x//50)] %5 is 0:
                if main_state.number[int(hero.y // 50) + 1][int(hero.x // 50)]  is 0:
                    main_state.number[int(hero.y // 50) + 1][int(hero.x // 50)] = 1
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)] = 0
                hero.horizontal = 5
        elif event == A_DOWN:
            if main_state.number[int(hero.y // 50)][int(hero.x // 50)-1] %5 is 0:
                if main_state.number[int(hero.y // 50)][int(hero.x // 50) - 1] is 0:
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)-1] = 1
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)] = 0
                hero.vertical = -5
            hero.dir = False
        elif event == S_DOWN:
            if main_state.number[int(hero.y // 50)-1][int(hero.x // 50)] %5 is 0:
                if main_state.number[int(hero.y // 50) - 1][int(hero.x // 50)]  is 0:
                    main_state.number[int(hero.y // 50) - 1][int(hero.x // 50)] = 1
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)] = 0
                hero.horizontal = -5
        elif event == D_DOWN:
            if main_state.number[int(hero.y // 50)][int(hero.x // 50)+1] %5 is 0:
                if main_state.number[int(hero.y // 50)][int(hero.x // 50) + 1] is 0:
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)+1] = 1
                    main_state.number[int(hero.y // 50)][int(hero.x // 50)] = 0
                hero.vertical = 5
            hero.dir = True
        elif event == W_UP:
            if main_state.number[int(hero.y//50)+1][int(hero.x//50)] %5 is 0:
                hero.horizontal = 5
        elif event == A_UP:
            if main_state.number[int(hero.y // 50)][int(hero.x // 50)-1] %5 is 0:
                hero.vertical = -5
        elif event == S_UP:
            if main_state.number[int(hero.y // 50) - 1][int(hero.x // 50)] %5 is 0:
                hero.horizontal = -5
        elif event == D_UP:
            if main_state.number[int(hero.y // 50)][int(hero.x // 50) + 1] %5 is 0:
                hero.vertical = 5
        hero.timer = 10

    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        game_framework.turn = False
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if hero.timer>0 :
            hero.x+=hero.vertical
            hero.y += hero.horizontal
            hero.timer-=1
        elif hero.timer==0:
            game_framework.turn = True
            hero.add_event(W_UP)


    @staticmethod
    def draw(hero):
        if hero.dir == True:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, -3.141592, 'v', hero.drax+25,100+ hero.dray+25,32, 50)
        else:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, 180*-3.141592 ,' ', hero.drax+25,100+ hero.dray+25,32,50)

class AttackState:
    @staticmethod
    def enter(hero, event):
        hero.bgm.play(1)
        hero.timer = 9
        pass

    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        game_framework.turn = False
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if hero.timer > 0:
            hero.timer -= 1
        elif hero.timer == 0:
            game_framework.turn = True
            hero.add_event(W_UP)

    @staticmethod
    def draw(hero):
        if hero.dir == True:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 405 * 1, 32, 57, -3.141592, 'v', hero.drax + 25,100 + hero.dray + 25, 34, 50)
        else:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 405 * 1, 32, 57, 180*-3.141592, ' ', hero.drax + 25,100 + hero.dray + 25, 34, 50)

next_state_table = {
    IdleState: {W_DOWN: RunState, A_DOWN: RunState, S_DOWN: RunState, D_DOWN: RunState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState,Left_Click:AttackState},
    RunState: {W_DOWN: IdleState, A_DOWN: IdleState, S_DOWN: IdleState, D_DOWN: IdleState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState,Left_Click:IdleState},
    AttackState:{W_DOWN: IdleState, A_DOWN: IdleState, S_DOWN: IdleState, D_DOWN: IdleState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState,Left_Click:AttackState}
}

class HERO:
    def __init__(self):
        self.x, self.y= 500,100
        self.HP,self.recovery_HP=100,0
        self.drax, self.dray=0,0
        self.state=0
        self.frame=0
        self.vertical = 0
        self.horizontal=0
        self.dir = True #true-right false-left
        self.timer=0
        self.image=load_image('Resource\character\Hero2.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.bgm = load_wav('Resource\Sound\punch1.wav')
        self.bgm.set_volume(30)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if self.timer==0:
                self.add_event(key_event)

    def draw(self):
        self.cur_state.draw(self)

    def attack(self):
        game_framework.turn = False
        self.add_event(Left_Click)
    def hit(self,power):
        self.HP -=power;

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.x>400 and self.x<2600+1:
            self.drax=400
        elif self.x>2600:
            self.drax=self.x-2200;
        else :
            self.drax=self.x
        if self.y>300 and self.y<2050+1:
            self.dray=300
        elif self.y>2050 :
            self.dray=self.y-1750
        else :
            self.dray=self.y
        if game_framework.turn is False and self.HP<100:
            self.recovery_HP+=1
        if self.recovery_HP > 60 and self.HP<100-3:
            self.recovery_HP-=60
            self.HP +=3

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
        self.image=load_image('Resource\character\star.png')

    def draw(self):
        if(self.state==0):# idle
            self.image.clip_draw(self.frame * 34 +2,1485 * 1, 31, 31, self.x,100+ self.y)
        elif(self.state==1): #running
            self.image.clip_draw(self.frame * 34 +2,1451 * 1, 31, 31, self.x,100+ self.y)
        elif (self.state == 2):  # running
            self.image.clip_draw(self.frame * 34 + 2, 1451 * 1, 31, 31, self.x, 100 + self.y)

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
