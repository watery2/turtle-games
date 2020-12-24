import turtle
import random
import math

wn = turtle.Screen()
wn.title("space")
wn.bgpic("spaceCopy.png")
wn.setup(height=600, width=800)
wn.tracer(0)
wn.addshape("spaceship3Copy.GIF")
wn.addshape("spaceship2Copy.GIF")
wn.addshape("bulletCopy.GIF")
wn.addshape("spaceshipanimCopy.GIF")
wn.addshape("spaceshipanim2Copy.GIF")
wn.addshape("spaceshipanim3Copy.GIF")
# player
player = turtle.Turtle()
player.speed(0)
player.shape('spaceship3Copy.GIF')
player.penup()
player.dy = 0
player.dx = 0
player.goto(0, -250)
player_looking_up = "looking_up"
# enemy
alienX_change = 0.4
number_of_aliens = 5
aliens = []
for i in range(number_of_aliens):
    aliens.append(turtle.Turtle())
for alien in aliens:
    alien.shape('spaceship2Copy.GIF')
    alien.penup()
    alien.speed(0)
    xa = random.randint(-200, 200)
    ya = random.randint(100,250)
    alien.setposition(xa,ya)
# the bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape('bulletCopy.GIF')
bullet.penup()
bullet.hideturtle()
bullet_state = "ready"
bullet_speed = 4
#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-300,260)
pen.write("score: 0 ",align="center",font=("courier", 24,"normal"))
score = 0
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
# movement
def move_right ():
    global player_looking_up
    player.shape('spaceshipanimCopy.GIF')
    player_looking_up = "looking_right"
    x = player.xcor()
    x += 20
    player.setx(x)
def move_left ():
    global player_looking_up
    player.shape('spaceshipanim2Copy.GIF')
    player_looking_up = "looking_left"
    x = player.xcor()
    x -= 20
    player.setx(x)
def look_up ():
    global player_looking_up
    player.shape('spaceshipanim3Copy.GIF')
    player_looking_up = "looking_up"

def fire ():
    global bullet_state
    if bullet_state == "ready" and player_looking_up == "looking_up":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
def Collision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

wn.listen()
wn.onkeypress(move_right,"d")
wn.onkeypress(move_left,"a")
wn.onkeypress(fire,"space")
wn.onkeypress(look_up,"w")
while True:


    # boarders
    if player.xcor() > 360:
        player.setx(360)
        player.dx *= -1

    if player.xcor() < -368:
        player.setx(-368)
        player.dx *= -1

# enemy movements
    for alien in aliens:
        xa = alien.xcor()
        xa += alienX_change
        alien.setx(xa)

        if alien.xcor() <= -375:
            for alien in aliens:
                alienX_change = 0.4
                ya = alien.ycor()
                ya -= 40
                alien.sety(ya)

        elif alien.xcor() >= 350:
            for alien in aliens:
                alienX_change = -0.4
                ya = alien.ycor()
                ya -= 40
                alien.sety(ya)

        if Collision(bullet, alien):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            xa = random.randint(-200,200)
            ya = random.randint(100,250)
            alien.setposition(xa, ya)
            score += 10
            pen.clear()
            pen.write("score: {} ".format(score), align="center", font=("courier", 24, "normal"))
        if Collision(player, alien):
            xa = random.randint(-200, 200)
            ya = random.randint(100, 250)
            for alien in aliens:
                alien.setposition(xa, ya)
            player.hideturtle()
            pen2.write("GAME OVER ", align="center", font=("courier", 34, "normal"))
    # bullet movement

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"



    wn.update()