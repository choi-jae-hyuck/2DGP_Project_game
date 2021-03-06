import game_framework
import main_state
import information_state
from pico2d import *


name = "TitleState"
image = None
bgm=None


def enter():
    global image,bgm
    image=load_image('Resource\First.png')
    bgm = load_music('Resource\Sound\Title.mp3')
    bgm.set_volume(30)
    bgm.repeat_play()


def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) ==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type)== (SDL_KEYDOWN):
                game_framework.change_state(information_state)


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 355, 213,400,300,800,600)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






