import pygame
import sys
import keyboard

clock = pygame.time.Clock()


def exit_conditions():
    from main import exit, player_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed(exit) or len(player_list) == 0:
            print("You died")
            pygame.quit()
            sys.exit()

def update_screen():
    from main import window, player, asteroid_group, blast_group
    player.update()
    asteroid_group.update()
    blast_group.update()
    pygame.display.flip()
    clock.tick(75)
    window.fill((0,0,0))

def draw():
    from main import window, player_group, asteroid_group, blast_group, bg
    from Scoring import show_score
    window.blit(bg, (0, 0))
    player_group.draw(window)
    asteroid_group.draw(window)
    blast_group.draw(window)
    show_score()

