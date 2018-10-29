from pico2d import *
import random
import map

class Floor:
    image1= None
    image2 = None
    image3 = None
    image4 = None
    def __init__(self):
        if Floor.image1==None :
            Floor.image1=load_image('dungeon_floor.png')
        elif Floor.image2==None :
            Floor.image2 = load_image('dungeon_floor2.png')
        elif Floor.image3 == None:
            Floor.image3 = load_image('dungeon_floor3.png')
        elif Floor.image4 == None:
            Floor.image4 = load_image('dungeon_floor4.png')

class Stair:
    image1=None
    image2=None
    def __init__(self):
        if Stair.image1==None:
            Stair.image1 = load_image('dungeon_stair.png')
        elif Stair.image2 == None:
            Stair.image2 = load_image('dungeon_stair2.png')

class Wall:
    image1=None
    image2=None
    def __init__(self):
        if Wall.image1==None:
            Wall.image1 = load_image('dungeon_wall.png')
        elif Wall.image2==None:
            Wall.image2 = load_image('dungeon_wall2.png')

def MapDraw(list,x,y,map_stage):
    wall=Wall()
    floor=Floor()
    stair=Stair()
    for i in range(y,y+12):
        for j in range(x,x+16):
            if map_stage == 1:
                if list[i][j]== 'floor':
                    Floor.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)
                elif list[i][j]=='wall':
                    Wall.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)
                elif list[i][j] == 'stair':
                    Stair.image1.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)
            elif map_stage == 2:
                if list[i][j]== 'floor':
                    Floor.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)
                elif list[i][j]=='wall':
                    Wall.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)
                elif list[i][j] == 'stair':
                    Stair.image2.clip_draw(0, 0, 41, 41, 25 + (j * 50), 25 + (i * 50), 50, 50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
gen=map.Generator()
gen.gen_level()
open_canvas()
running=True
while running:
    clear_canvas()
    MapDraw(gen.level,0,0,1)
    update_canvas()
    handle_events()
    delay(0.05)
close_canvas()
