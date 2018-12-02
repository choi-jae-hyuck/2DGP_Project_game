import random
import json
import os

from pico2d import *
import game_framework
import game_world
import keyboard_mouse
import game_over_state
import game_end_state

from hero_star import HERO
from tiles import Tile
from fish import Fish
from bird import Bird

name = "MainState"
hero = None
mouse =None
number =[]
fish=[]
bird=[]
global mouse_x,mouse_y,keyboard
keyboard,mouse_x,mouse_y=None,0,0
bgm=None
open_lock=None

def enter():
    global bgm,open_lock
    bgm = load_music('Resource\Sound\Background.mp3')
    open_lock=load_wav('Resource\Sound\Open_lock.wav')
    open_lock.set_volume(128)
    bgm.set_volume(30)
    bgm.repeat_play()
    global hero, tiles,fish,bird
    tiles= Tile()
    hero = HERO()
    fish = [Fish() for i in range(10)]
    bird =[Bird() for i in range(5)]

    global number
    number = [[0] * 60 for i in range(45)]
    for i in range(0,45):
        for j in range(0,60):
            if tiles.dungeon.level[i][j] is 'floor':
                number[i][j]=0
            elif tiles.dungeon.level[i][j] is 'stone':
                number[i][j]=9
            elif tiles.dungeon.level[i][j] is 'wall':
                number[i][j]=9
            elif tiles.dungeon.level[i][j] is 'stair':
                number[i][j]=6

    start = True
    while (start):#hero setting
        i = random.randint(0+1, 45 - 1)
        j = random.randint(0+1, 60 - 1)
        if number[i][j] is 0:
            hero.x = j * 50
            hero.y = i * 50
            number[i][j]=1
            start = False
    for k in range(10):
        while(fish[k].setting is False):
            i = random.randint(0+1, 45 - 1)
            j = random.randint(0+1, 60 - 1)
            if number[i][j] is 0 and fish[k].setting is False:
                fish[k].x = j * 50
                fish[k].y = i * 50
                number[i][j] = 2
                fish[k].setting=True
    for k in range(5):
        while(bird[k].setting is False):
            i = random.randint(0+1, 45 - 1)
            j = random.randint(0+1, 60 - 1)
            if number[i][j] is 0 and bird[k].setting is False:
                bird[k].x = j * 50
                bird[k].y = i * 50
                number[i][j] = 2
                bird[k].setting=True



    game_world.add_object(tiles, 0)
    game_world.add_object(hero, 1)
    game_world.add_objects(fish,1)
    game_world.add_objects(bird,1)

    global mouse,keyboard
    mouse = keyboard_mouse.Mouse()
    keyboard=keyboard_mouse.Keyboard()
    game_world.add_object(mouse, 1)
    game_world.add_object(keyboard,1)
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
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT and mouse.select ==True and game_framework.turn is True:
            game_framework.turn = False
            hero.attack()
            for fiser in fish:
                fiser.hit(mouse_x,mouse_y)
            for birds in bird:
                birds.hit(mouse_x,mouse_y)

        else:
            hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
        for fiser in fish:
            if fiser.HP<=0:
                fish.remove(fiser)
                number[fiser.y//50][fiser.x//50]=0
                game_world.remove_object(fiser)
                tiles.lock -=1
        for birds in bird:
            if birds.HP<=0:
                bird.remove(birds)
                number[birds.y//50][birds.x//50]=0
                game_world.remove_object(birds)
                tiles.lock -= 1
    if number[int(hero.y // 50)][int(hero.x // 50)] is 5:
        game_framework.push_state(game_end_state)
    if hero.HP < 0 + 1:
        game_framework.push_state(game_over_state)
    if tiles.lock<=0:
        for i in range(0, 45):
            for j in range(0, 60):
                if number[i][j] is 6:
                    number[i][j]=5
                    open_lock.play(1)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






