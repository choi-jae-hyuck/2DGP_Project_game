from pico2d import *
import random
import map
import hero_star
import game_framework
import game_world
import main_state


class Floor:
    image1= None
    image2 = None
    image3 = None
    image4 = None
    def __init__(self):
        if Floor.image1==None :
            Floor.image1=load_image('Resource\dungeontile\dungeon_floor.png')
        if Floor.image2==None :
            Floor.image2 = load_image('Resource\dungeontile\dungeon_floor2.png')
        if Floor.image3 == None:
            Floor.image3 = load_image('Resource\dungeontile\dungeon_floor3.png')
        if Floor.image4 == None:
            Floor.image4 = load_image('Resource\dungeontile\dungeon_floor4.png')
class Stair:
    image1=None
    image2=None
    def __init__(self):
        if Stair.image1==None:
            Stair.image1 = load_image('Resource\dungeontile\dungeon_stair.png')
        if Stair.image2 == None:
            Stair.image2 = load_image('Resource\dungeontile\dungeon_stair2.png')

class Wall:
    image1=None
    image2=None
    def __init__(self):
        if Wall.image1==None:
            Wall.image1 = load_image('Resource\dungeontile\dungeon_wall.png')
        if Wall.image2==None:
            Wall.image2 = load_image('Resource\dungeontile\dungeon_wall2.png')

class Tile:
    def __init__(self):
        self.dungeon=map.Generator()
        self.dungeon.gen_level()
        self.back_image=None
        if self.back_image is None:
            self.back_image=load_image('Resource\dungeontile\Back.png')
        self.UI_image = None
        if self.UI_image is None:
            self.UI_image = load_image('Resource\dungeontile\Board_ui.png')
        self.HP_bar=None
        if self.HP_bar is None:
            self.HP_bar = load_image('Resource\dungeontile\HP_bar.png')
        self.x=0 //50
        self.y=0 //50
        self.scrollx=0
        self.scrolly=0
        self.mapstage=1

    def draw(self):
        #map 은 y60 x45임
        wall = Wall()
        floor = Floor()
        stair = Stair()
        if self.x>8 and self.x<52:
            self.scrollx=self.x-8
        elif self.x>52-1:
            self.scrollx=44
        else :
            self.scrollx=0
        if self.y>6 and self.y<41:
            self.scrolly=self.y-6
        elif self.y>30:
            self.scrolly=35
        else :
            self.scrolly=0

        self.back_image.clip_draw(0, 0, 41, 41,400,300,800, 600)
        self.UI_image.clip_draw(10, 40, 245, 75, 400, 50, 850, 100)
        self.HP_bar.clip_draw(50, 90, 3, 3, 140+main_state.hero.HP*0.7, 60, 1.7* main_state.hero.HP, 40)
        self.HP_bar.clip_draw(20, 50, 450, 120, 200, 60, 200, 50)

        for i in range(0,0+10):
            for j in range(0,0+16):
                if self.mapstage == 1:
                    if self.dungeon.level[self.scrolly+i][self.scrollx+j]== 'floor':
                        Floor.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[self.scrolly+i][self.scrollx+j]=='wall':
                        Wall.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[self.scrolly+i][self.scrollx+j] == 'stair':
                        Stair.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                elif self.mapstage == 2:
                    if self.dungeon.level[self.scrolly+i][self.scrollx+j]== 'floor':
                        Floor.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[self.scrolly+i][self.scrollx+j]=='wall':
                        Wall.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[self.scrolly+i][self.scrollx+j] == 'stair':
                        Stair.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)

    def update(self):
        self.x=int(main_state.hero.x//50)
        self.y=int(main_state.hero.y//50)
