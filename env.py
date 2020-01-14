import numpy
from config import *
from ascii_stuff import *

class Cloud:

	def __init__(self,x,y):
		self.rows = len(ascii_cloud)
		self.columns = len(ascii_cloud[0])
		self.image = ascii_cloud
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "cloud"

	def move(self):
		self.y -= 1
		if self.y == -10:
			self.delete = 1

class Coin:

	def __init__(self,x,y):
		self.rows = len(ascii_coin)
		self.columns = len(ascii_coin[0])
		self.image = ascii_coin
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "coin"

	def move(self):
		self.y -= 1
		if self.y == -10:
			self.delete = 1

	def chk(self,x,y):
		for i in range(4):
			for j in range(3):
				if self.check_if_got(x+i,y-2+j):
					return 1
		return 0

	def check_if_got(self,x,y):
		if x==self.x and y==self.y:
			return 1
		if x==self.x and y==self.y+1:
			return 1
		if x==self.x+1 and y==self.y:
			return 1
		if x==self.x+1 and y==self.y+1:
			return 1
		return 0