import sys,numpy
from config import *
from colorama import Fore, Back, Style, init, deinit

class Board:

	def __init__(self):
		self.__rows = ROWS
		self.__columns = COLUMNS
		self.__time = TIME
		self.__lives = LIVES
		self.__score = SCORE
		self.__board_arr = numpy.array([[' ']*self.__columns])
		self.__objs = []
		self.__border = SKY_LAND_BORDER
		self.__hbh = HEADER_BORDER_H
		self.__hbw = HEADER_BORDER_W
		self.__mag_time = 0
		self.__fr = FRAME_RATE
		self.__speed_boost_time = 0
		self.__shield = 0

	def check_prints(self,i,j):
		if self.__board_arr[i][j] == 'y':
			print(Style.BRIGHT+Back.YELLOW+' ',end="")
			return 1
		if self.__board_arr[i][j]==':':
			print(Style.DIM+Fore.RED+'O',end="")
			return 1
		if self.__board_arr[i][j]=='b':
			print(Style.BRIGHT+Back.RED+' ',end="")
			return 1
		if self.__board_arr[i][j]=='w':
			print(Style.BRIGHT+Back.WHITE+' ',end="")
			return 1
		if self.__board_arr[i][j]=='r':
			print(Style.BRIGHT+Back.RED+' ',end="")
			return 1
		return 0

	def print_board(self):
		init()
		print('\033[H')
		for i in range(self.__columns+2):
			print(Style.BRIGHT+Back.WHITE+' ',end="")
		print()
		for i in range(self.__rows):
			print(Style.BRIGHT+Back.WHITE+' ',end="")
			print(Style.RESET_ALL,end="")
			for j in range(self.__columns):
				if self.check_prints(i,j)==1:
					continue
				if (i==self.__hbh and j<=self.__hbw) or (i<self.__hbh and j==self.__hbw):
					print(Style.BRIGHT+Back.WHITE+' ',end="")
					continue
				else:
					print(Style.RESET_ALL,end="")
				if self.__border > i:
					print(Style.BRIGHT+Back.BLUE+self.__board_arr[i][j],end="")
				else:
					print(Style.BRIGHT+Back.GREEN+self.__board_arr[i][j],end="")
			print(Style.BRIGHT+Back.WHITE+' ')
		for i in range(self.__columns+2):
			print(Style.BRIGHT+Back.WHITE+' ',end="")
		print(Style.RESET_ALL,end="")
		print()
		deinit()

	def get_num_str(self,s):
		if s==0:
			return ['0']
		tmp = []
		while s>0:
			tmp.append(str(int(s%10)))
			s /= 10
			s = int(s)
		tmp.reverse()
		return tmp

	def update_corner(self,arr):
		sc = ['S','C','O','R','E',' ','=']
		li = ['L','I','V','E','S',' ','=']
		tl = ['T','I','M','E',' ','=']
		lol = 3
		arr[1:2,lol:len(sc)+lol] = sc
		arr[2:3,lol:len(li)+lol] = li
		arr[3:4,lol:len(tl)+lol] = tl
		tmp = self.get_num_str(self.__score)
		arr[1:2,len(sc)+1+lol:len(sc)+1+len(tmp)+lol] = tmp
		tmp = self.get_num_str(self.__time)
		arr[3:4,len(tl)+1+lol:len(tl)+1+len(tmp)+lol] = tmp
		for i in range(self.__lives):
			arr[2:3,len(li)+1+lol+2*i:len(li)+2+lol+2*i] = "❤"

	def update_corner2(self,arr,x):
		li = ['L','I','V','E','S',' ','=']
		lol = 105
		arr[1:2,lol:len(li)+lol] = li
		tmp = self.get_num_str(x)
		arr[1:2,len(li)+1+lol] = '❤'
		arr[1:2,len(li)+3+lol] = 'x'
		arr[1:2,len(li)+4+lol:len(li)+4+len(tmp)+lol] = tmp
		arr[0:3,102:103] = 'w'
		arr[3:4,102:120] = 'w'

	def check_ball(self,arr):
		arr1 = []
		arr2 = []

		for i in range(1,len(arr)):
			if arr[i].get_name()=="ball":
				arr1.append(i)

		for i in range(1,len(arr)):
			if arr[i].get_name()=="bar" or arr[i].get_name()=="enemy":
				arr2.append(i)

		for i in range(len(arr1)):
			for j in range(len(arr2)):
				if arr[arr1[i]].get_delete():
					break
				if arr[arr2[j]].get_delete()==0 and arr[arr1[i]].chk(arr[arr2[j]]):
					arr[arr1[i]].delt()
					arr[arr2[j]].delt()
					self.__score += 2

		arr2 = []
		for i in range(1,len(arr)):
			if arr[i].get_name()=="dragon":
				arr2.append(i)
		if len(arr2):
			for i in range(len(arr1)):
				if arr[arr1[i]].chk(arr[arr2[0]]):
					arr[arr1[i]].delt()
					arr[arr2[0]].dec_lives()

		arr1 = []

		for i in range(1,len(arr)):
			if arr[i].get_name()=="ice_ball":
				arr1.append(i)

		for i in range(len(arr1)):
			if arr[arr1[i]].chk(arr[0]):
				arr[arr1[i]].delt()
				self.__lives -= 1

		return 0

	def update_board(self,arr):
		
		arr.sort(key=lambda x:x.get_priority())

		self.__board_arr = numpy.array([[' ']*self.__columns])
		for i in range(self.__rows):
			self.__board_arr = numpy.vstack([self.__board_arr,[' ']*self.__columns])

		tmparr = []

		self.check_ball(arr)

		l1 = []

		for i in range(1,len(arr)):
			if arr[i].get_name()=="coin" and arr[i].chk(arr[0]):
				self.__score += 5
				tmparr.append(i)
				continue
			if (arr[i].get_name()=="bar" or arr[i].get_name()=="enemy") and arr[i].chk(arr[0]) and self.__shield==0:
				self.__lives -= 1
			if arr[i].get_name()=="magnet":
				if arr[i].chk(arr[0]):
					self.__mag_time += (MAGNET_TIME*FRAME_RATE)
			if arr[i].get_name()=="boost":
				if arr[i].chk(arr[0]):
					self.__speed_boost_time += (SPEED_BOOST_TIME*self.__fr)
			if arr[i].get_name()=="shield":
				self.__shield = arr[i].update_shield( arr[0].get_x() - 1 , arr[0].get_y() - 2 , self.__time )
			for j in range(arr[i].get_rows()):
				for k in range(arr[i].get_columns()):
					if arr[i].get_x()+j>=0 and arr[i].get_x()+j<self.__rows and arr[i].get_y()+k>=0 and arr[i].get_y()+k<self.__columns:
						self.__board_arr[arr[i].get_x()+j][arr[i].get_y()+k] = arr[i].get_image()[j][k]
			if arr[i].get_name() == "coin" and self.__mag_time>0:
				arr[i].move_magnet(arr[0])
			else:
				if arr[i].get_name()=="dragon":
					arr[i].move_dragon(arr[0],arr)
					l1.append(arr[i])
					self.update_corner2(self.__board_arr,arr[i].get_lives())
				elif arr[i].get_name()=="magnet2":
					arr[i].move(arr[0])
				else:
					arr[i].move()
			if arr[i].get_delete() == 1:
				tmparr.append(i)

		for j in range(arr[0].get_rows()):
			for k in range(arr[0].get_columns()):
				if arr[0].get_y()+k>=0 and arr[0].get_y()+k<self.__columns:
					self.__board_arr[arr[0].get_x()+j][arr[0].get_y()+k] = arr[0].get_image()[j][k]
		k = 0
		for i in tmparr:
			arr.pop(i-k)
			k += 1

		self.update_corner(self.__board_arr)
		if self.__mag_time > 0:
			self.__mag_time -= 1
		if arr[0].get_can_shoot() > 0:
			arr[0].dec_shoot()
		if self.__speed_boost_time > 0:
			self.__speed_boost_time -= 1
		if self.__lives == 0 or self.__time == 0:
			self.exit_game(0)
		if len(l1):
			if l1[0].get_lives() == 0:
				self.exit_game(1)
		self.print_board()

	def add_game_over(self,x):
		s = "GAME  OVER"
		arr = []
		for i in s:
			arr.append(i)
			arr.append(" ")
		self.__board_arr[13:14,50:50+len(arr)] = arr
		if x:
			s = "YOU WIN"
			f = 1
		else:
			s = "YOU LOSE"
			f = 0
		arr = []
		for i in s:
			arr.append(i)
			arr.append(" ")
		self.__board_arr[14:15,52+f:52+f+len(arr)] = arr

	def exit_game(self,x):
		self.add_game_over(x)
		self.print_board()
		exit()

	def update_time(self):
		self.__time -= 1

	def get_fr(self):
		return self.__fr

	def get_speed_boost_time(self):
		return self.__speed_boost_time

	def get_time(self):
		return self.__time

Main_Board = Board()