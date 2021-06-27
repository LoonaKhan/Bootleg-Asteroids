from Sprites import Sprite
from random import randint, choice, uniform

skulls = [
    "psychic.png",
    "laser.png",
    "normie.png",
    "sniper.png",
    "speedy.png",
    "tank.png"
]

def spawn_astroid(x = None, y = None, scale = [1.0,1.0]):
    from main import asteroid_group, asteroids_list, spawn_rate
    chance = randint(0,spawn_rate)
    if chance == spawn_rate or (x is not None and y is not None):

        if scale[0] < 0.25 or scale[1] < 0.25: return
        if scale[0]> 0.85:
            size = uniform(0.25, 0.75)
            scale = [size, size]
        asteroid = Sprite(x,y, pic_path=choice(skulls), scale=scale)
        asteroid_group.add(asteroid)
        asteroids_list.append(asteroid)