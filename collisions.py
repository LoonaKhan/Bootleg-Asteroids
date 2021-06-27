import pygame

def collisions(list1, list2):
    for sprite in list1:
        from main import player_list
        for asteroid in list2:
            col = pygame.sprite.collide_rect(sprite, asteroid)
            if col:
                rect = sprite.rect
                scale = asteroid.scale
                if sprite not in player_list:
                    from Scoring import inc_score, score_msg
                    inc_score(1000)
                    score_msg(rect[0], rect[1])

                sprite.kill(); list1.remove(sprite)
                asteroid.kill(); list2.remove(asteroid)

                from asteroids import spawn_astroid
                scale = [scale[0]-0.25, scale[1]-0.25]
                spawn_astroid(rect[0], rect[1], scale)
                break

