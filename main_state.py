import random
import json
import os

from pico2d import *
import game_framework
import game_world

from hero_star import HERO
from tiles import Tile
from fish import Fish

name = "MainState"

hero = None

def enter():
    global hero, tiles,fish
    tiles= Tile()
    hero = HERO()
    fish = Fish()
    start=True
    while(start):
        i=random.randint(0,45-1)
        j=random.randint(0,60-1)
        if tiles.dungeon.level[i][j] == 'floor':
            #hero.x=j*50+25
            #hero.y=i*50+25
            hero.x=300
            hero.y=300
            start=False

    game_world.add_object(tiles, 0)
    game_world.add_object(hero, 1)
    game_world.add_object(fish,1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






