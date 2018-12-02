import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
bgm=None
information_time = 0.0

def enter():
    global image,bgm
    image=load_image('Resource\Information.png')


def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 355, 213,400,300,800,600)
    update_canvas()







def update():
    global information_time
    if (information_time > 3.0):
        information_time = 0
        # game_framework.quit()
        game_framework.push_state(main_state)
    delay(0.01)
    information_time+= 0.01


def pause():
    pass


def resume():
    pass






