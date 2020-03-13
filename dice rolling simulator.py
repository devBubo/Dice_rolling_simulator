from random import randint
from tkinter import *
root=Tk()
root.title('Dice rolling simulator')
canvas=Canvas()
canvas.pack()
width=800
height=600
canvas.config(width=width,height=height)
click_x=5000
click_y=5000
dice_1=PhotoImage(file='dice_1.png')
dice_2=PhotoImage(file='dice_2.png')
dice_3=PhotoImage(file='dice_3.png')
dice_4=PhotoImage(file='dice_4.png')
dice_5=PhotoImage(file='dice_5.png')
dice_6=PhotoImage(file='dice_6.png')
roll_again_button=PhotoImage(file='Roll again.png')
dice_rolloute=[dice_1,dice_2,dice_3,dice_4,dice_5,dice_6]


def Click(coordinate):
    global click_x
    global click_y
    click_x = coordinate.x
    click_y = coordinate.y

canvas.bind('<Button 1>', Click)
dice1 = randint(0, 5)
dice2 = randint(0, 5)

while True:


    canvas.create_image(width/2-100, height/2-56, anchor=NW,image=dice_rolloute[dice1])
    canvas.create_image(width / 2 + 50, height / 2 - 56, anchor=NW, image=dice_rolloute[dice2])
    canvas.create_image(width / 2 - 70,height / 2 + 80,anchor=NW, image=roll_again_button)
    canvas.update()

