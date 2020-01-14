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

class Parent:

	def move(self):
		self.y -= 1
		if self.y == -10:
			self.delete = 1

	def chk(self,obj):
		arr = []
		for i in range(obj.r):
			arr.append([0]*obj.c)

		for j in range(obj.rows):
			for k in range(obj.columns):
				if obj.y+k>=0 and obj.y+k<obj.c and obj.image[j][k]!=' ':
					arr[obj.x+j][obj.y+k] = 1

		for j in range(self.rows):
			for k in range(self.columns):
				if self.x+j>=0 and self.x+j<obj.r and self.y+k>=0 and self.y+k<obj.c and self.image[j][k]!=' ':
					if arr[self.x+j][self.y+k]==1:
						return 1

		return 0

class Coin(Parent):

	def __init__(self,x,y):
		self.rows = len(ascii_coin)
		self.columns = len(ascii_coin[0])
		self.image = ascii_coin
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "coin"

class Bars(Parent):

	def __init__(self,x,y,p):
		self.rows = len(ascii_bars[p])
		self.columns = len(ascii_bars[p][0])
		self.image = ascii_bars[p]
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "bar"