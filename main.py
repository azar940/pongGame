# imported
import turtle

# config win
win = turtle.Screen()
win.title("Ping Pong By Aziz")
win.bgcolor("#1D1B1B")
win.setup(width=1200, height=800)
win.tracer(0) # stops the window from updating auto


#objects
#lebara1
lebara1 = turtle.Turtle()
lebara1.speed(0) # lebara yata7arak yadhar 3ala xaxa bi a3la sor3a ay aktar men 60fps/s
lebara1.shape("square")
lebara1.color("#687BCE")
lebara1.penup()
lebara1.goto(-560, 0)
widl1 = 8
lebara1.shapesize(stretch_wid=widl1, stretch_len=1)

#lebara2
lebara2 = turtle.Turtle()
lebara2.speed(0) # lebara yata7arak yadhar 3ala xaxa bi a3la sor3a ay aktar men 60fps/s
lebara2.shape("square")
lebara2.color("#C45454")
lebara2.penup()
lebara2.goto(560, 0)
widl2 = 8
lebara2.shapesize(stretch_wid=widl2, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0) # lebara yata7arak yadhar 3ala xaxa bi a3la sor3a ay aktar men 60fps/s
ball.shape("square")
ball.color("#F6F6F6")
ball.penup()
ball.goto(0, 0)
bldx = 0.4
bldy = 0.4
ball.dx = bldx
ball.dy = bldy

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 370)
score.write("Player 1 : {}   VS   Player 2 : {}".format(score1, score2), align="center", font=100)





#functions
def lebara1_up():
    y = lebara1.ycor()
    y += 30
    lebara1.sety(y)

def lebara1_down():
    y = lebara1.ycor()
    y -= 30
    lebara1.sety(y)

def lebara2_up():
    y = lebara2.ycor()
    y += 30
    lebara2.sety(y)

def lebara2_down():
    y = lebara2.ycor()
    y -= 30
    lebara2.sety(y)

#keyboard bindings
win.listen()

win.onkeypress(lebara1_up, "z")
win.onkeypress(lebara1_down, "s")

win.onkeypress(lebara2_up, "Up")
win.onkeypress(lebara2_down, "Down")

#game loop
while True:
    win.update() # updates the screen everytime the loop run
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border check
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1


    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1 : {}   VS   Player 2 : {}".format(score1, score2), align="center", font=100)

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1 : {}   VS   Player 2 : {}".format(score1, score2), align="center", font=100)


    #lebara o ball
    if (ball.xcor() > 540 and ball.xcor() < 550) and (ball.ycor() < lebara2.ycor() + 70 and ball.ycor() > lebara2.ycor() -70):
        ball.setx(540)
        ball.dx *= -1
    if (ball.xcor() < -540 and ball.xcor() > -550) and (ball.ycor() < lebara1.ycor() + 70 and ball.ycor() > lebara1.ycor() -70):
        ball.setx(-540)
        ball.dx *= -1

