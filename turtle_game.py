import turtle as t
import random as rd

t.bgcolor('yellow')


catepillar = t.Turtle()
catepillar.shape('square')
catepillar.speed(0)
catepillar.penup()
catepillar.color('green')
catepillar.hideturtle()

gum = t.Turtle()
gum_shape = ((0, 0), (15, 2), (18, 7), (20, 20), (7, 18), (2, 15))
t.register_shape('gum', gum_shape)
gum.shape('gum')
gum.color('#E52DD9')
gum.penup()
gum.speed(0)
gum.hideturtle()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center',
                  font=('Arial', 18, 'bold'))
text_turtle.hideturtle()
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.speed(0)


def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = catepillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside


def place_gum():
    gum.hideturtle()
    gum.setx(rd.randint(-200, 200))
    gum.sety(rd.randint(-200, 200))
    gum.showturtle()


def display_score(current_score):
    score_turtle.clear()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 70
    score_turtle.setposition(x, y)
    score_turtle.write(str(current_score), align='right',
                       font=('Arial', 40, 'bold'))


def game_over():
    catepillar.color('yellow')
    gum.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center',
            font=('Arial', 30, 'normal'))


def startgame():
    global game_started
    if game_started:
        return
        # when you use "pass" it just renews the game every time you press "space"
    game_started = True

    score = 0

    text_turtle.clear()

    catepillar_speed = 2
    catepillar_length = 3
    catepillar.shapesize(1, catepillar_length, 1)
    catepillar.showturtle()
    display_score(score)
    place_gum()

    while True:
        catepillar.forward(catepillar_speed)
        if catepillar.distance(gum) < 20:
            catepillar_speed += 2
            catepillar_length += 1
            catepillar.shapesize(1, catepillar_length, 1)
            place_gum()
            score += 1
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():
    if catepillar.heading() == 0 or catepillar.heading() == 180:
        catepillar.setheading(90)


def move_down():
    if catepillar.heading() == 0 or catepillar.heading() == 180:
        catepillar.setheading(270)


def move_right():
    if catepillar.heading() == 90 or catepillar.heading() == 270:
        catepillar.setheading(0)


def move_left():
    if catepillar.heading() == 90 or catepillar.heading() == 270:
        catepillar.setheading(180)


t.onkey(startgame, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()
