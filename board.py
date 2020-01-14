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

	def print_board(self):
		init()
		print('\033[H')
		for i in range(self.columns+2):
			print(Back.WHITE+' ',end="")
		print()
		for i in range(self.rows):
			print(Back.WHITE+' ',end="")
			print(Style.RESET_ALL,end="")
			for j in range(self.columns):
				if self.board_arr[i][j] == 'y':
					print(Back.YELLOW+' ',end="")
					continue
				if (i==self.hbh and j<=self.hbw) or (i<self.hbh and j==self.hbw):
					print(Back.WHITE+' ',end="")
					continue
				else:
					print(Style.RESET_ALL,end="")
				if self.border > i:
					print(Back.BLUE+self.board_arr[i][j],end="")
				else:
					print(Back.GREEN+self.board_arr[i][j],end="")
			print(Back.WHITE+' ')
		for i in range(self.columns+2):
			print(Back.WHITE+' ',end="")
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
		lol = 3
		arr[1:2,lol:len(sc)+lol] = sc
		arr[2:3,lol:len(li)+lol] = li
		tmp = self.get_num_str(self.score)
		arr[1:2,len(sc)+1+lol:len(sc)+1+len(tmp)+lol] = tmp
		for i in range(self.lives):
			arr[2:3,len(li)+1+lol+2*i:len(li)+2+lol+2*i] = "❤"

	def update_board(self,arr):
		self.board_arr = numpy.array([[' ']*self.columns])
		for i in range(self.rows):
			self.board_arr = numpy.vstack([self.board_arr,[' ']*self.columns])

		tmparr = []

		for i in range(len(arr)):
			if arr[i].name=="mandalorian":
				for j in range(arr[i].rows):
					for k in range(arr[i].columns):
						if arr[i].y+k>=0 and arr[i].y+k<self.columns:
							self.board_arr[arr[i].x+j][arr[i].y+k] = arr[i].image[j][k]
				continue
			if arr[i].chk(arr[0].x,arr[0].y):
				self.score += 5
				tmparr.append(i)
				continue
			for j in range(arr[i].rows):
				for k in range(arr[i].columns):
					if arr[i].y+k>=0 and arr[i].y+k<self.columns:
						self.board_arr[arr[i].x+j][arr[i].y+k] = arr[i].image[j][k]
			arr[i].move()
			if arr[i].delete == 1:
				tmparr.append(i)

		k = 0
		for i in tmparr:
			arr.pop(i-k)
			k += 1

		self.update_corner(self.board_arr)

Main_Board = Board()