from pico2d import *
import random
import map
import game_framework
import game_world

global gen

class Floor:
    image1= None
    image2 = None
    image3 = None
    image4 = None
    def __init__(self):
        if Floor.image1==None :
            Floor.image1=load_image('dungeontile\dungeon_floor.png')
        elif Floor.image2==None :
            Floor.image2 = load_image('dungeontile\dungeon_floor2.png')
        elif Floor.image3 == None:
            Floor.image3 = load_image('dungeontile\dungeon_floor3.png')
        elif Floor.image4 == None:
            Floor.image4 = load_image('dungeontile\dungeon_floor4.png')
class Stair:
    image1=None
    image2=None
    def __init__(self):
        if Stair.image1==None:
            Stair.image1 = load_image('dungeontile\dungeon_stair.png')
        elif Stair.image2 == None:
            Stair.image2 = load_image('dungeontile\dungeon_stair2.png')

class Wall:
    image1=None
    image2=None
    def __init__(self):
        if Wall.image1==None:
            Wall.image1 = load_image('dungeontile\dungeon_wall.png')
        elif Wall.image2==None:
            Wall.image2 = load_image('dungeontile\dungeon_wall2.png')

class Tile:
    def __init__(self):
        self.dungeon=map.Generator()
        self.dungeon.gen_level()
        self.x=0
        self.y=0
        self.mapstage=1

    def draw(self):
        wall = Wall()
        floor = Floor()
        stair = Stair()
        for i in range(self.y,self.y+10):
            for j in range(self.x,self.x+16):
                if self.mapstage == 1:
                    if self.dungeon.level[i][j]== 'floor':
                        Floor.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[i][j]=='wall':
                        Wall.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[i][j] == 'stair':
                        Stair.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                elif self.mapstage == 2:
                    if self.dungeon.level[i][j]== 'floor':
                        Floor.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[i][j]=='wall':
                        Wall.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)
                    elif self.dungeon.level[i][j] == 'stair':
                        Stair.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 125 + (i * 50), 50, 50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

tile=Tile()
open_canvas()
running=True
while running:
    clear_canvas()
    tile.draw()
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()
