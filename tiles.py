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
        self.x=0 //50
        self.y=0 //50
        self.scrollx=0
        self.scrolly=0
        self.mapstage=1
        self.bgm = load_music('Resource\Sound\Background.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

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
