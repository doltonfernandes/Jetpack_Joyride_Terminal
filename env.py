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

	def move(self):
		self.y -= 1
		if self.y == -10:
			self.delete = 1