

score = 0
check_points = [25_000]

def inc_score(inc_value):
    global score
    score+=inc_value
    print(score)

def show_score():
    from main import window, txt_x, txt_y, font
    global score
    show_score = font.render(f"SCORE: {score}", True,(255,255,255))
    window.blit(show_score,(txt_x, txt_y))

def score_msg(x,y):
    from main import window, font
    message = font.render("SCORE  +1000", True, (255,255,255))
    window.blit(message, (x,y))


def difficulty():
    from main import spawn_rate, max_asteroids
    global score, check_points

    for check_point in check_points:
        if score < check_point: return [spawn_rate, max_asteroids]

        if spawn_rate > 5: spawn_rate -= 5
        else: spawn_rate = 5
        if max_asteroids < 100: max_asteroids += 5
        else: max_asteroids = 100
        check_points.append(check_point+5_000)
        check_points.remove(check_point)
        return [spawn_rate, max_asteroids]
