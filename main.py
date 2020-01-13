from random import randint
from board import *
from texts import *
from env import *
from objs import *
from key_press import *
import time,sys,signal
from os import system

def signal_handler(sig, frame):
    exit()

signal.signal(signal.SIGINT, signal_handler)

system("clear")

obj_arr = []
x = Jet_Boy()
x.jb_init()
obj_arr.append(x)

if __name__ == "__main__":
	print_welcome_screen()
	inp = input()
	system("clear")
	fr = 1/FRAME_RATE
	cnt = 0
	while 1:
		Main_Board.update_board(obj_arr)
		Main_Board.print_board()
		x = key_press(sys.argv[1:],fr)
		obj_arr[0].check_char(x)
		cnt += 1
		if cnt == 40:
			cnt = 0
			obj_arr.append(Coin(randint(5,10),120))