import keyboard
import pygame
from random import randint, uniform
import time

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x = None, pos_y = None, pic_path = None, scale = [1.0,1.0]):
        """
        Loads in a sprite with the given image at the given location

        :param pos_x: x coordinate. none by default
        :param pos_y: y coordinate. also none by default
        :param pic_path: directory of the image
        :param angle: angle the sprite will move in
        """
        super().__init__()

        # if x and y are not given, it is an asteroid and its position is determined at random
        # however, if they are given, x and y are given normally
        if pos_x is None and pos_y is None:
            from main import sc_h, sc_w
            chance = randint(0, 1)
            if chance == 1: self.pos_x = randint(0, sc_w); self.pos_y = 0
            if chance == 0: self.pos_y = randint(0, sc_h); self.pos_x = 0
        else:
            self.pos_x = pos_x; self.pos_y = pos_y

        #creates the image and image rect. allows for scaling
        self.scale = scale
        self.image = pygame.image.load(pic_path)
        self.size = self.image.get_rect().size; self.size = [self.size[0], self.size[1]]
        self.size[0]*=scale[0]; self.size[1]*=scale[1]
        self.size[0], self.size[1] = int(self.size[0]), int(self.size[1])
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x,self.pos_y]

        #sets the x and y variables
        self.x, self.y = 2*uniform(-1,1), 2*uniform(-1,1)
        if self.x == 0: self.x = 2*uniform(-1,1)
        if self.y == 0: self.y = 2*uniform(-1,1)

        self.prev_time = 0
        self.now = time.time()

    def update(self):
        from main import sc_h, sc_w, blast_list
        if self.pos_x <= 0: self.pos_x = sc_w
        elif self.pos_x >= sc_w: self.pos_x = 0
        elif self.pos_y <= 0: self.pos_y = sc_h
        elif self.pos_y >= sc_h: self.pos_y = 0

        self.pos_x+=self.x; self.pos_y += self.y

        self.rect.center = [self.pos_x, self.pos_y]


        self.prev_time = time.time()
        if self.prev_time - self.now > 1 and self in blast_list:
            blast_list.remove(self); self.kill()

    def inputs(self):
        """
        recieves the players inputs and then modifies their x and y vars. ONLY FOR PLAYER.
        """
        from main import up, down, left, right, speed
        self.x, self.y = 0,0

        if keyboard.is_pressed(up) and keyboard.is_pressed(left):
            self.x, self.y = -speed,-speed
        elif keyboard.is_pressed(up) and keyboard.is_pressed(right):
            self.x, self.y = speed,-speed
        elif keyboard.is_pressed(down) and keyboard.is_pressed(left):
            self.x, self.y = -speed,speed
        elif keyboard.is_pressed(down) and keyboard.is_pressed(right):
            self.x, self.y = speed,speed
        elif keyboard.is_pressed(up):
            self.x, self.y = 0,-speed
        elif keyboard.is_pressed(down):
            self.x, self.y = 0,speed
        elif keyboard.is_pressed(left):
            self.x, self.y = -speed,0
        elif keyboard.is_pressed(right):
            self.x, self.y = speed,0

    def shoot(self):
        from main import blast_list, blast_group
        blast = Sprite(self.pos_x, self.pos_y, "heart blast.png", scale=[3.0,3.0])
        blast.x, blast.y = 2.5*self.x, 2.5*self.y
        blast_group.add(blast)
        blast_list.append(blast)