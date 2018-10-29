from pico2d import *
import random


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

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
            


open_canvas()
star = STAR()
hero = HERO()

running = True
x = 800 // 2
star_frame=0
hero_frame = 0

while running:
    clear_canvas()

    hero.update()
    star.update()

    hero.draw()
    star.draw()
    
    update_canvas()

    handle_events()
    

    delay(0.05)

close_canvas()

