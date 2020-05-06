#!/usr/local/bin/python3

import turtle


def polygon(sides, length, shape):
    for x in range(sides):
        shape.forward(length)
        shape.left(360 / sides)



# create a screem
window = turtle.Screen()
# Set the background color
window.bgcolor("lightgreen")
# create turtle
shape = turtle.Turtle()
# set turtle color
shape.color("blue")
shape.pensize(3)
# take input
sides = int(input("How many sides do you want? Use digits: "))
length = 50
polygon(sides, length, shape)
sides = int(input("How many sides do you want? Use digits: "))