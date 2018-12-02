import game_framework
from pico2d import *
import random
import game_world

import main_state

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Bird:
    def __init__(self):
        self.x, self.y= 500,400
        self.HP=10
        self.state=0
        self.frame=0
        self.timer=0
        self.image=load_image('Resource\character\enemy1.png')
        self.Hitting_draw_opacify = 1
        self.dir=True
        self.attack=False
        self.setting=False
        self.doing_first=True

    def draw(self):
        self.image.opacify(self.Hitting_draw_opacify)
        if self.dir is True and self.y+25-main_state.tiles.scrolly*50+100>100:
            if self.state is 0:# idle
                self.image.clip_composite_draw(int(self.frame) * 45 + 1, 498 * 1, 43, 31, 180 * 3.141592 / 180, 'v', self.x + 25 - main_state.tiles.scrollx * 50,self.y + 25 - main_state.tiles.scrolly * 50 + 100, 45, 45)
            if self.state is 1:# running
                self.image.clip_composite_draw(int(self.frame) * 46 + 1, 430 * 1, 46, 31, 180 * 3.141592 / 180, 'v',self.x + 25 - main_state.tiles.scrollx * 50,self.y + 25 - main_state.tiles.scrolly * 50 + 100, 45, 45)
            elif self.state is 2: #attack
                self.image.clip_composite_draw(int(self.frame) * 43 + 4, 466 * 1, 38, 31, 180 * 3.141592 / 180, 'v',self.x + 25 - main_state.tiles.scrollx * 50,self.y + 25 - main_state.tiles.scrolly * 50 + 100, 45, 45)
        elif  self.dir is False and self.y+25-main_state.tiles.scrolly*50+100>100:
            if self.state is 0:  # idle
                self.image.clip_composite_draw(int(self.frame) * 45 + 1, 498 * 1, 43, 31, 0 * 3.141592/180, ' ',self.x + 25 - main_state.tiles.scrollx * 50, self.y + 25 - main_state.tiles.scrolly * 50 + 100, 45, 45)
            if self.state is 1:  # running
                self.image.clip_composite_draw(int(self.frame) * 46 + 1, 430 * 1, 46, 31, 33 * 3.141592/180, ' ', self.x+25-main_state.tiles.scrollx*50,  self.y+25-main_state.tiles.scrolly*50+100, 45, 45)
            elif self.state is 2:  # attack
                self.image.clip_composite_draw(int(self.frame) * 43 + 4, 466 * 1, 38, 31, 0 * 3.141592/180, ' ', self.x+25-main_state.tiles.scrollx*50, self.y+25-main_state.tiles.scrolly*50+100, 45, 45)


    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.state is 0:
            self.frame=(self.frame)%4
        elif self.state is 1:
            self.frame=(self.frame)%3
        elif self.state is 2:
            self.frame=(self.frame)%5

        if main_state.hero.x<self.x:
            self.dir = False
        else:
            self.dir =True


        if game_framework.turn is False:
            if self.attack is True:
                self.state=2
                if self.doing_first is True:
                    main_state.hero.hit(20)
                    self.doing_first=False
                pass
            elif self.attack is False:
                if self.movement is 1:
                    if self.doing_first is True:
                        main_state.number[self.y // 50 + 1][self.x // 50]=2
                        main_state.number[self.y // 50][self.x // 50]=0
                        self.doing_first=False
                    self.y+=5
                elif self.movement is 2:
                    if self.doing_first is True:
                        main_state.number[self.y // 50 - 1][self.x // 50]=2
                        main_state.number[self.y // 50][self.x // 50]=0
                        self.doing_first=False
                    self.y-=5
                elif self.movement is 3:
                    if self.doing_first is True:
                        main_state.number[self.y // 50][self.x // 50-1]=2
                        main_state.number[self.y // 50][self.x // 50]=0
                        self.doing_first=False
                    self.x-=5
                elif self.movement is 4:
                    if self.doing_first is True:
                        main_state.number[self.y // 50][self.x // 50+1]=2
                        main_state.number[self.y // 50][self.x // 50]=0
                        self.doing_first=False
                    self.x+=5


        elif game_framework.turn is True:
            self.state = 0
            self.Hitting_draw_opacify =1
            while True:
                self.doing_first=True
                self.movement = random.randint(1, 4)  # 상하좌우
                if self.movement is 1 and self.y<44*50:
                    if main_state.number[self.y // 50 + 1][self.x // 50] is 0:
                        break
                elif self.movement is 2 and self.y>0*50:
                    if main_state.number[self.y // 50 - 1][self.x // 50] is 0:
                        break
                elif self.movement is 3 and self.x>0*50:
                    if main_state.number[self.y // 50][self.x // 50 - 1] is 0:
                        break
                elif self.movement is 4 and self.x<59*50:
                    if main_state.number[self.y // 50][self.x // 50 + 1] is 0:
                        break

            if main_state.hero.x-50<=self.x <=main_state.hero.x+50 and main_state.hero.y-50<=self.y <=main_state.hero.y+50:
                self.attack=True
            else :
                self.attack=False

    def handle_event(self, event):
       pass

    def hit(self,x,y):
        if (main_state.tiles.scrollx*50+x)//50 is self.x//50 and(main_state.tiles.scrolly*50+y-100)//50 is self.y//50:
            self.HP -=5
            self.state=1
            self.Hitting_draw_opacify=0.7

    def add_event(self, event):
      pass