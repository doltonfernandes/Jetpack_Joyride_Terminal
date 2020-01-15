import sys,numpy
from config import *
from colorama import Fore, Back, Style, init, deinit

class Board:

	def __init__(self):
		self.rows = ROWS
		self.columns = COLUMNS
		self.time = TIME
		self.lives = LIVES
		self.score = SCORE
		self.board_arr = numpy.array([[' ']*self.columns])
		self.objs = []
		self.border = SKY_LAND_BORDER
		self.hbh = HEADER_BORDER_H
		self.hbw = HEADER_BORDER_W
		self.mag_time = 0
		self.fr = FRAME_RATE
		self.speed_boost_time = 0
		self.shield = 0

	def check_prints(self,i,j):
		if self.board_arr[i][j] == 'y':
			print(Style.BRIGHT+Back.YELLOW+' ',end="")
			return 1
		if self.board_arr[i][j]==':':
			print(Style.DIM+Fore.RED+'O',end="")
			return 1
		if self.board_arr[i][j]=='b':
			print(Style.BRIGHT+Back.RED+' ',end="")
			return 1
		if self.board_arr[i][j]=='w':
			print(Style.BRIGHT+Back.WHITE+' ',end="")
			return 1
		if self.board_arr[i][j]=='r':
			print(Style.BRIGHT+Back.RED+' ',end="")
			return 1
		return 0

	def print_board(self):
		init()
		print('\033[H')
		for i in range(self.columns+2):
			print(Style.BRIGHT+Back.WHITE+' ',end="")
		print()
		for i in range(self.rows):
			print(Style.BRIGHT+Back.WHITE+' ',end="")
			print(Style.RESET_ALL,end="")
			for j in range(self.columns):
				if self.check_prints(i,j)==1:
					continue
				if (i==self.hbh and j<=self.hbw) or (i<self.hbh and j==self.hbw):
					print(Style.BRIGHT+Back.WHITE+' ',end="")
					continue
				else:
					print(Style.RESET_ALL,end="")
				if self.border > i:
					print(Style.BRIGHT+Back.BLUE+self.board_arr[i][j],end="")
				else:
					print(Style.BRIGHT+Back.GREEN+self.board_arr[i][j],end="")
			print(Style.BRIGHT+Back.WHITE+' ')
		for i in range(self.columns+2):
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
		tmp = self.get_num_str(self.score)
		arr[1:2,len(sc)+1+lol:len(sc)+1+len(tmp)+lol] = tmp
		tmp = self.get_num_str(self.time)
		arr[3:4,len(tl)+1+lol:len(tl)+1+len(tmp)+lol] = tmp
		for i in range(self.lives):
			arr[2:3,len(li)+1+lol+2*i:len(li)+2+lol+2*i] = "❤"

	def check_ball(self,arr):
		arr1 = []
		arr2 = []

		for i in range(1,len(arr)):
			if arr[i].name=="ball":
				arr1.append(i)

		for i in range(1,len(arr)):
			if arr[i].name=="bar" or arr[i].name=="enemy":
				arr2.append(i)

		for i in range(len(arr1)):
			for j in range(len(arr2)):
				if arr[arr1[i]].delete:
					break
				if arr[arr2[j]].delete==0 and arr[arr1[i]].chk(arr[arr2[j]]):
					arr[arr1[i]].delete = 1
					arr[arr2[j]].delete = 1
					self.score += 2
		return 0

	def update_board(self,arr):
		
		arr.sort(key=lambda x:x.priority)

		self.board_arr = numpy.array([[' ']*self.columns])
		for i in range(self.rows):
			self.board_arr = numpy.vstack([self.board_arr,[' ']*self.columns])

		tmparr = []

		self.check_ball(arr)

		for i in range(1,len(arr)):
			if arr[i].name=="coin" and arr[i].chk(arr[0]):
				self.score += 5
				tmparr.append(i)
				continue
			if (arr[i].name=="bar" or arr[i].name=="enemy") and arr[i].chk(arr[0]) and self.shield==0:
				self.lives -= 1
			if arr[i].name=="magnet":
				if arr[i].chk(arr[0]):
					self.mag_time += (MAGNET_TIME*FRAME_RATE)
			if arr[i].name=="boost":
				if arr[i].chk(arr[0]):
					self.speed_boost_time += (SPEED_BOOST_TIME*self.fr)
			if arr[i].name=="shield":
				self.shield = arr[i].update_shield( arr[0].x - 1 , arr[0].y - 2 )
			for j in range(arr[i].rows):
				for k in range(arr[i].columns):
					if arr[i].x+j>=0 and arr[i].x+j<self.rows and arr[i].y+k>=0 and arr[i].y+k<self.columns:
						self.board_arr[arr[i].x+j][arr[i].y+k] = arr[i].image[j][k]
			if arr[i].name == "coin" and self.mag_time>0:
				arr[i].move_magnet(arr[0])
			else:
				if arr[i].name=="dragon":
					arr[i].move_dragon(arr[0])
				else:
					arr[i].move()
			if arr[i].delete == 1:
				tmparr.append(i)

		for j in range(arr[0].rows):
			for k in range(arr[0].columns):
				if arr[0].y+k>=0 and arr[0].y+k<self.columns:
					self.board_arr[arr[0].x+j][arr[0].y+k] = arr[0].image[j][k]
		k = 0
		for i in tmparr:
			arr.pop(i-k)
			k += 1

		self.update_corner(self.board_arr)
		if self.mag_time > 0:
			self.mag_time -= 1
		if arr[0].can_shoot > 0:
			arr[0].can_shoot -= 1
		if self.speed_boost_time > 0:
			self.speed_boost_time -= 1
		if self.lives == 0 or self.time == 0:
			self.exit_game()
		self.print_board()

	def add_game_over(self):
		s = "GAME OVER"
		arr = []
		for i in s:
			arr.append(i)
			arr.append(" ")
		self.board_arr[13:14,50:50+len(arr)] = arr

	def exit_game(self):
		self.add_game_over()
		self.print_board()
		exit()

	def update_time(self):
		self.time -= 1

Main_Board = Board()