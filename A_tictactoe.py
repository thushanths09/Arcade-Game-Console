#GP106 PROJECT
#Arcade Game Console
#Game 01: Tic Tac Toe
#E/20/401, E/20/402, E/20/403, E/20/404
from pyfirmata import *
from pyfirmata import util
import time

# creating the board
board = Arduino('COM9')

# setting up the direction keys
move = board.get_pin('d:11:i')
click = board.get_pin('d:12:i')
buzzer = board.get_pin('d:13:o')
quit = board.get_pin('a:1:i')

# setting up the led lights for playing
l1 = board.get_pin('d:2:o')
l2 = board.get_pin('d:3:o')
l3 = board.get_pin('d:4:o')
l4 = board.get_pin('d:5:o')
l5 = board.get_pin('d:6:o')
l6 = board.get_pin('d:7:o')
l7 = board.get_pin('d:8:o')
l8 = board.get_pin('d:9:o')
l9 = board.get_pin('d:10:o')

# LED Layout
led_lights = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
led_layout = [
    [l1, l2, l3],
    [l4, l5, l6],
    [l7, l8, l9]
]

# setting up position of led and creating the set of selcted leds
pos = [0, 0]
clicked_led_1 = []
clicked_led_2 = []
player1 = 'X'
player2 = 'O'

# creating iterator to read the button
it = util.Iterator(board)
it.start()
move.enable_reporting()
click.enable_reporting()

#function for winning
def win():
    win_matches=[[l1,l2,l3], [l4,l5,l6], [l7,l8,l9], [l1,l4,l7], [l2,l5,l8], [l3,l6,l9], [l1,l5,l9], [l3,l5,l7]]
    for i in win_matches:
        if i == clicked_led_1:
            print("PLAYER 1 WIN")
            return True
        elif i == clicked_led_2:
            print("PLAYER 2 WIN")
            return True

#number of turns and current player
present_player = player1
turn = 1

#initial score
player1_score = 0
player2_score = 0

#Main Loop for Game
while True:
    # reading the button states
    move_state = move.read()
    click_state = click.read()

    # initially turning off the lights
    for led in led_lights:
        led.write(0)

    # turn on the position led if it is not selected and switching players led
    pos_led = led_layout[pos[0]][pos[1]]
    if pos_led not in (clicked_led_1 or clicked_led_2):
        if present_player == player1:
            pos_led.write(1)
            time.sleep(0.2)
        elif present_player == player2:
            pos_led.write(1)
            time.sleep(0.1)
            pos_led.write(0)
            time.sleep(0.1)
            pos_led.write(1)
            time.sleep(0.1)
        else:
            pass

    #moving controls
    if move_state == 1:
        pos[1] += 1
        if pos[1] > 2:
            pos[1] = 0
            pos[0] += 1
            if pos[0] > 2:
                pos[0] = 0
        time.sleep(0.1)

    # turn on the selected led
    if click_state == 1:
        clicked_led = led_layout[pos[0]][pos[1]]
        #switching players
        if present_player == player1:
            clicked_led_1.append(clicked_led)
            clicked_led.write(1)
            time.sleep(0.5)
            present_player = player2
        elif present_player == player2:
            clicked_led_2.append(clicked_led)
            clicked_led.write(1)
            time.sleep(0.2)
            clicked_led.write(0)
            time.sleep(0.2)
            clicked_led.write(1)
            time.sleep(0.2)
            clicked_led.write(0)
            time.sleep(0.2)
            present_player = player1
        else:
            pass
        turn += 1
        time.sleep(0.1)
    else:
        pass

    #check winner
    if win():
        buzzer.write(1)
        time.sleep(2)
        buzzer.write(0)
        if present_player == player1:
            player1_score += 1
        else:
            player2_score += 1
        break

    #draw(no winner)
    if turn == 9:
        print("DRAW")
        break
    time.sleep(0.1)

#quitting the game
if quit.read() == 1:
    print("SCORE")
    print("-------")
    print("Player 1 : ",player1_score)
    print("Player 2 : ",player2_score)
    board.exit()
