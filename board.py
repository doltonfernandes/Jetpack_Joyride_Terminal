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
		arr[1:2,1:len(sc)+1] = sc
		arr[2:3,1:len(li)+1] = li
		tmp = self.get_num_str(self.score)
		arr[1:2,len(sc)+2:len(sc)+2+len(tmp)] = tmp
		tmp = self.get_num_str(self.lives)
		arr[2:3,len(li)+2:len(li)+2+len(tmp)] = tmp

	def mark_mandalorian(self,x,y):
		self.board_arr[x][y]='O'
		self.board_arr[x+1][y]='|'
		self.board_arr[x+1][y-1]='|'
		self.board_arr[x+1][y-2]='/'
		self.board_arr[x+2][y]='\\'
		self.board_arr[x+2][y-1]='\\'
		self.board_arr[x+3][y]='L'
		self.board_arr[x+3][y-1]='L'

	def update_board(self,arr):
		self.board_arr = numpy.array([[' ']*self.columns])
		for i in range(self.rows):
			self.board_arr = numpy.vstack([self.board_arr,[' ']*self.columns])

		tmparr = []

		for i in range(len(arr)):
			if i==0:
				self.mark_mandalorian(arr[i].x,arr[i].y)
				continue
			if arr[i].offset >= arr[i].columns:
				tmparr.append(i)
				continue
			for j in range(self.rows):
				for k in range(self.columns):
					if k + arr[i].offset<arr[i].columns and arr[i].image[j][k + arr[i].offset]!=' ':
						self.board_arr[j][k] = arr[i].image[j][k + arr[i].offset]
			arr[i].offset += 1

		k = 0
		for i in tmparr:
			arr.pop(i-k)
			k += 1

		self.update_corner(self.board_arr)

Main_Board = Board()