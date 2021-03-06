from random import randint
from board import *
from texts import *
from objs import *
from key_press import *
from os import system
import sys

class Game:

	def __init__(self):
		self.__obj_arr = []
		self.__neck_arr = []
		self.__cnt = 0
		self.__cnt1 = 0
		self.__cnt2 = 0
		self.__cnt3 = 0
		self.__cnt4 = 0

	def start_game(self):
		self.__obj_arr = []
		x = Jet_Boy()
		x.jb_init()
		self.__obj_arr.append(x)
		f = 1
		while 1:
			Main_Board.update_board(self.__obj_arr,self.__neck_arr)
			fr = Main_Board.get_fr()
			if Main_Board.get_speed_boost_time() > 0:
				fr *= 3
			x = K.key_press(sys.argv[1:],1/fr)
			self.__obj_arr[0].check_char(self.__neck_arr,x,self.__obj_arr,Main_Board.get_time())
			self.increment()
			if Main_Board.get_time() == DRAGON_ENTER_TIME and f:
				self.__obj_arr.append(Dragon(5,155))
				f = 0
			self.check1()
			self.gravity()
			if Main_Board.get_time() < DRAGON_ENTER_TIME + 40:
				continue
			self.add_coin()
			self.add_bars_and_enemies()
			self.add_magnets_and_boost()

	def increment(self):
		self.__cnt += 1
		self.__cnt1 += 1
		self.__cnt2 += 1
		self.__cnt3 += 1
		self.__cnt4 += 1

	def check1(self):
		if self.__cnt == 5:
			Main_Board.update_time()
			self.__cnt = 0

	def gravity(self):
		self.__obj_arr[0].move_down(Main_Board.get_time())

	def add_coin(self):
		if self.__cnt3 == 17:
			self.__cnt3 = 0
			self.__obj_arr.append(Coin(randint(6,40),200))

	def add_bars_and_enemies(self):
		if self.__cnt1 == 25:
			self.__cnt1 = 0
			self.__obj_arr.append(Bars(randint(25,28),200,randint(0,3)))
			if randint(0,1):
				x = Enemy()
				x.enemy_init(40,200)
				self.__obj_arr.append(x)

	def add_magnets_and_boost(self):
		if self.__cnt4 == 300:
			self.__cnt4 = 0
			x = randint(0,2)
			if x==0:
				self.__obj_arr.append(Magnet(15,200))
			elif x==1:
				self.__obj_arr.append(Magnet_Assignment(randint(7,38),200))
			else:
				self.__obj_arr.append(Boost(15,200))

game = Game()