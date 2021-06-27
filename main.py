import time

import keyboard
import pygame
from Gameloop_functions import update_screen, exit_conditions, draw
from Sprites import Sprite
from asteroids import spawn_astroid
from Scoring import inc_score,difficulty
from collisions import collisions

sc_w, sc_h = 1000,1000; mid_x, mid_y = sc_w/2, sc_h/2
pygame.init()
window = pygame.display.set_mode((sc_w,sc_h))
font = pygame.font.SysFont("Arial", 32)
txt_x, txt_y = 10,10

#GLOBAL VARIABLES======================================================================================================#
#Keybinds
up = "Up"
down = "Down"
left = "Left"
right = "Right"
shoot = "Shift"
exit = "Escape"

#Player Variables
speed = 4

#Background
bg = pygame.image.load("background.jpg")

#Asteroid spawn-related will change as the player's score increases
max_asteroids = 5
spawn_rate = 100 #how often an asteroid will spawn in frames.

#SPRITES
player_group = pygame.sprite.Group() #player stuff
player = Sprite(mid_x, mid_y, "heart.png")
player_group.add(player)
player_list = [player]

asteroid_group = pygame.sprite.Group()
asteroids_list = []

blast_group = pygame.sprite.Group()
blast_list =[]
max_blasts = 20

#MUSIC=================================================================================================================#

music =pygame.mixer.music
music.load("music.wav")
music.set_volume(0.2)

#MAIN GAME LOOP========================================================================================================#
init_time = 0
music.play(-1)
while True:
    now = time.time()
    #checks if the exit conditions are fulfilled
    exit_conditions()

    #draws and gets the player coordinates
    draw()
    player.inputs()

    #generates asteroids
    if len(asteroids_list) < max_asteroids: spawn_astroid()

    #score
    inc_score(1)

    #shoot
    if keyboard.is_pressed(shoot) and len(blast_list)< max_blasts and now-init_time >0.1: player.shoot(); init_time = time.time()

    #check collisions
    shot = collisions(blast_list, asteroids_list)
    collisions(player_list, asteroids_list)

    #difficulty
    ast_stuff = difficulty()
    spawn_rate = ast_stuff[0]; max_asteroids = ast_stuff[1]

    #updates screen
    update_screen()
