from pico2d import *
import random
# Game object class here


class Grass: # 클래스 이름은 대문자로 시작
    def __init__(self): # self: 생성된 객체를 카리킨다
        self.image = load_image('grass.png')

    # 행위를 정의함
    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Big_ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')

    def update(self):
        while self.y > 70:
            self.y -= 5

    def draw(self):
        self.image.draw(self.x, self.y)


class Small_ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        pass
    
    def draw(self):
        self.image.draw(self.x, self.y)
        while self.y > 65:
            self.y -= 5



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world

    global big_balls
    global small_balls

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    big_balls = [Big_ball() for i in range(10)]
    world += big_balls
    small_balls = [Small_ball() for i in range(10)]
    world += small_balls


def update_world():
    for o in world:
        o.update()

def render_world():
   clear_canvas()
   for o in world:
       o.draw()
   update_canvas()


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()

# initialization code

# game main loop code

# finalization code

close_canvas()
