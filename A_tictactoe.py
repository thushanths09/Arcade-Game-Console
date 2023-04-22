from pyfirmata import *
from pyfirmata import util
import time


def win():
    return 5


def draw():
    return 7


def loose():
    return 8


# creating the board
board = Arduino('COM9')

# setting up the direction keys
up = board.get_pin('d:9:i')
down = board.get_pin('d:10:i')
left = board.get_pin('d:11:i')
right = board.get_pin('d:12:i')
click = board.get_pin('d:13:i')

# setting up the led lights for playing
l1 = board.get_pin('d:0:o')
l2 = board.get_pin('d:1:o')
l3 = board.get_pin('d:2:o')
l4 = board.get_pin('d:3:o')
l5 = board.get_pin('d:4:o')
l6 = board.get_pin('d:5:o')
l7 = board.get_pin('d:6:o')
l8 = board.get_pin('d:7:o')
l9 = board.get_pin('d:8:o')

# LED Layout
led_lights = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
led_layout = [
    [l1, l2, l3],
    [l4, l5, l6],
    [l7, l8, l9]
]

# setting up position of led and creating the set of selcted leds
pos = [1, 1]
clicked_leds = set()

# creating iterator to read the button
it = util.Iterator(board)
it.start()

while True:
    # initially turning off the lights
    for led in led_lights:
        led.write(0)

    # turn on the position led if it is not selected
    pos_led = led_layout[pos[0][pos[1]]]
    if pos_led not in clicked_leds:
        board.digital[pos_led].write(1)

    # reading the button states
    up_state = up.read()
    down_state = down.read()
    left_state = left.read()
    right_state = right.read()
    click_state = click.read()
    l5.write(1)

    # controls
    # moving up
    if up_state == 1 and down_state == 0 and left_state == 0 and right_state == 0 and pos[0] > 0:
        pos[0] -= 1
        time.sleep(0.2)
    # moving down
    elif up_state == 0 and down_state == 1 and left_state == 0 and right_state == 0 and pos[0] < (len(led_layout) - 1):
        pos[0] += 1
        time.sleep(0.2)
    # moving left
    elif up_state == 0 and down_state == 0 and left_state == 1 and right_state == 0 and pos[1] > 0:
        pos[1] -= 1
        time.sleep(0.2)
    # moving right
    elif up_state == 0 and down_state == 0 and left_state == 0 and right_state == 1 and pos[1] < (len(led_layout) - 1):
        pos[1] += 1
        time.sleep(0.2)
    # turn on the selected led
    elif click_state == 1:
        clicked_led = led_layout[pos[0][pos[1]]]
        clicked_led.write(1)
        clicked_leds.add(clicked_led)
    else:
        pass
