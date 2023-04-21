from pyfirmata import *
import time

#creating the board
board=Arduino('COM9')

#setting up the direction keys
up=board.get_pin('a:0:i')
down=board.get_pin('a:1:i')
left=board.get_pin('a:2:i')
down=board.get_pin('a:3:i')
click=board.get_pin('a:4:i')

#setting up the led lights for playing
l1=board.get_pin('d:0:o')
l2=board.get_pin('d:1:o')
l3=board.get_pin('d:2:o')
l4=board.get_pin('d:3:o')
l5=board.get_pin('d:4:o')
l6=board.get_pin('d:5:o')
l7=board.get_pin('d:6:o')
l8=board.get_pin('d:7:o')
l9=board.get_pin('d:8:o')


def win():
    return 5
def draw():
    return 7
def loose():
    return 8
