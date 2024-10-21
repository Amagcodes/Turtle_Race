import turtle
import random
import time

#turtle class
while(True):
    num = int(input("Enter the number of turtles(2-10):"))

    if(num >= 2 and num <=10):
        print("Press the spacebar to start")
        break

colours = ["red", "yellow", "blue", "lightgreen", "cyan", "orange", "pink", "purple", "magenta", "white"]
i=0
players = []
    
wn = turtle.Screen()
wn.title("Turtle Race")
wn.bgcolor("green")
for x in range(num):
    player = turtle.Turtle()
    player.speed(0)
    player.shape("turtle")
    player.color(colours[i])
    i+=1
    player.penup()
    y = random.randint(-230,230)
    player.goto(-300,y)
    player.pendown()
    players.append(player)

def finish_line():
    turtle.color("white")
    turtle.speed(0)
    turtle.shape("square")
    turtle.penup()
    turtle.goto(300,280)
    turtle.right(90)
    for x in range(18):
        turtle.goto(300,(280 - (x * 20 * 2)))
        turtle.stamp()
    for x in range(18):
        turtle.goto(300 + 20,(320 - 20) - (x * 20 * 2))
        turtle.stamp()
    turtle.color("black")
    for x in range(18):
        turtle.goto(300, (300 - (x * 20 * 2)))
        turtle.stamp()
    for x in range(18):
        turtle.goto(301 + 20, (300 - 20) - (x * 20 * 2))
        turtle.stamp()
    

def run():
    yes = True
    while (yes==True):
        for player in players:
            player.forward(random.randint(1,10))
            if player.xcor() > 300:
                print("The winning turtle is: ", player.color()[0])
                player.shapesize(2,2)
                yes = False
    
finish_line()
wn.listen()
wn.onkeypress(run, "space")
wn.mainloop()
