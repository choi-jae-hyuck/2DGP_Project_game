from pico2d import *
import random
import game_framework
import game_world

W_DOWN, A_DOWN, S_DOWN, D_DOWN,W_UP, A_UP, S_UP, D_UP = range(8)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

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
class IdleState:

    @staticmethod
    def enter(hero, event):
        hero.velocity=0
        if event == W_DOWN:
            hero.velocity += 5
        elif event == A_DOWN:
            hero.velocity += -5
        elif event == S_DOWN:
            hero.velocity += -5
        elif event == D_DOWN:
            hero.velocity += 5
        elif event == W_UP:
            hero.velocity += -5
        elif event == A_UP:
            hero.velocity += 5
        elif event == S_UP:
            hero.velocity += 5
        elif event == D_UP:
            hero.velocity += -5
        hero.timer=10

    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if(hero.timer>0):
            hero.x+=hero.velocity
            hero.timer-=1

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55, -3.141592, 'v', hero.x, hero.y,40, 50)
        else:
            hero.image.clip_composite_draw(int(hero.frame) * 41 + 1, 1140 * 1, 40, 55, 180*-3.141592, ' ', hero.x, hero.y,40, 50)


class RunState:

    @staticmethod
    def enter(hero, event):
        hero.velocity = 0
        if event == W_DOWN:
            hero.velocity += 5
        elif event == A_DOWN:
            hero.velocity += -5
        elif event == S_DOWN:
            hero.velocity += -5
        elif event == D_DOWN:
            hero.velocity += 5
        elif event == W_UP:
            hero.velocity += -5
        elif event == A_UP:
            hero.velocity += 5
        elif event == S_UP:
            hero.velocity += 5
        elif event == D_UP:
            hero.velocity += -5
        hero.dir = clamp(-5,hero.velocity,5)

    @staticmethod
    def exit(hero, event):
        if event == None:
            pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        hero.x = clamp(25, hero.x, 1600 - 25)

    @staticmethod
    def draw(hero):
        if hero.dir == 1:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, -3.141592, 'v', hero.x, hero.y,32, 50)
        else:
            hero.image.clip_composite_draw(int(hero.frame) * 33 + 1, 1081 * 1, 32, 57, 180*-3.141592 ,' ', hero.x, hero.y,32,50)


next_state_table = {
    IdleState: {W_DOWN: RunState, A_DOWN: RunState, S_DOWN: RunState, D_DOWN: RunState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState},
    RunState: {W_DOWN: IdleState, A_DOWN: IdleState, S_DOWN: IdleState, D_DOWN: IdleState,W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState}
}

class HERO:
    def __init__(self):
        self.x, self.y= 500,100
        self.state=0
        self.frame=0
        self.velocity = 0
        self.dir = 1
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

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
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
