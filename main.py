from random import randint
from board import *
from texts import *
from objs import *
from key_press import *
import time,sys,signal
from os import system

def signal_handler(sig, frame):
	pass

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
	cnt = 0
	cnt1 = 0
	cnt2 = 0
	cnt3 = 0
	cnt4 = 0
	while 1:
		Main_Board.update_board(obj_arr)
		fr = Main_Board.fr
		if Main_Board.speed_boost_time > 0:
			fr *= 4
		x = K.key_press(sys.argv[1:],1/fr)
		if x=='m':
			obj_arr.append(Shield())
		obj_arr[0].check_char(x,obj_arr)
		cnt += 1
		cnt1 += 1
		cnt2 += 1
		cnt3 += 1
		cnt4 += 1
		lim = 40
		if cnt == FRAME_RATE:
			Main_Board.update_time()
			cnt = 0
		if cnt2 == 6:
			cnt2 = 0
			obj_arr[0].move_down()
		if cnt3 == 17:
			cnt3 = 0
			obj_arr.append(Coin(randint(5,27),120))
		if cnt1 == lim:
			cnt1 = 0
			lim = randint(40,80)
			obj_arr.append(Bars(randint(5,18),120,randint(0,3)))
			x = Enemy()
			x.enemy_init(29,120)
			obj_arr.append(x)
		if cnt4 == 300:
			cnt4 = 0
			obj_arr.append(Magnet(10,120))