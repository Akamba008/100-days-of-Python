import colorgram as c
import turtle as t
import random

# PROGRAM TO EXTRACT COLORS FROM AN IMAGE USING THE COLORMODE PACKAGE
# def extracted_colors(number):
#     color_list = []
#     colors = c.extract('image.jpg', number)
#     for color in range(number):
#         color_tuple = (colors[color].rgb.r, colors[color].rgb.g, colors[color].rgb.b)
#         color_list.append(color_tuple)
#     print(color_list)
#
#
# extracted_colors(30)

color_list = [(237, 234, 227), (239, 231, 236), (231, 234, 240), (230, 239, 234), (203, 161, 102), (205, 166, 24), (151, 58, 92), (121, 181, 203), (223, 206, 112), (144, 27, 50), (50, 15, 26), (10, 20, 46), (184, 154, 168), (22, 105, 159), (51, 18, 15), (49, 122, 72), (11, 28, 21), (167, 72, 48), (69, 164, 97), (144, 30, 22), (116, 179, 158), (211, 178, 198), (160, 205, 211), (183, 97, 113), (185, 102, 94), (32, 47, 108), (161, 208, 201), (8, 104, 48), (232, 203, 5), (222, 173, 168)]
t.colormode(255)
tom = t.Turtle()
tom.speed("fastest")
screen = t.Screen()

tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

original_x_coordinate = tom.position()[0]
x = original_x_coordinate
y = tom.position()[1]

for row in range(10):
    for col in range(10):
        tom.dot(20, random.choice(color_list))
        x += 50
        tom.goto(x, y)
    x = original_x_coordinate
    y += 50
    tom.goto(x,y)

screen.exitonclick()