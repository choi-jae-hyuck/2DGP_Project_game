import random
import json
import os

from pico2d import *
import game_framework
import game_world
import keyboard_mouse

from hero_star import HERO
from tiles import Tile
from fish import Fish

name = "MainState"
hero = None
mouse =None
number =[]
fish=[]

def enter():
    global hero, tiles,fish
    tiles= Tile()
    hero = HERO()
    fish = [Fish() for i in range(10)]

    global number
    number = [[0] * 60 for i in range(45)]
    for i in range(0,45-1):
        for j in range(0,60-1):
            if tiles.dungeon.level[i][j] is 'floor':
                number[i][j]=0
            elif tiles.dungeon.level[i][j] is 'stone':
                number[i][j]=9
            elif tiles.dungeon.level[i][j] is 'wall':
                number[i][j]=9

    start = True
    while (start):#hero setting
        i = random.randint(0+1, 45 - 2)
        j = random.randint(0+1, 60 - 2)
        if number[i][j] is 0:
            hero.x = j * 50
            hero.y = i * 50
            number[i][j]=1
            start = False
    for k in range(10):
        while(fish[k].setting is False):
            i = random.randint(0+1, 45 - 2)
            j = random.randint(0+1, 60 - 2)
            if number[i][j] is 0 and fish[k].setting is False:
                fish[k].x = j * 50
                fish[k].y = i * 50
                number[i][j] = 2
                fish[k].setting=True



    game_world.add_object(tiles, 0)
    game_world.add_object(hero, 1)
    game_world.add_objects(fish,1)

    global mouse
    mouse = keyboard_mouse.Mouse()
    game_world.add_object(mouse, 0)
    hide_cursor()

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
                mouse_x,mouse_y = event.x, get_canvas_height() - 1 - event.y
        else:
            hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






