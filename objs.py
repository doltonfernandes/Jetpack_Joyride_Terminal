from config import *
from ascii_stuff import *
import numpy

class Person:

	def __init__(self):
		self.r = ROWS
		self.c = COLUMNS
		self.offset = 0
		self.x = 0
		self.y = 0
		self.name = ""
		self.image = []

class Jet_Boy(Person):

	def jb_init(self):
		self.x = 29
		self.y = 10
		self.rows = len(ascii_mandalorian)
		self.columns = len(ascii_mandalorian[0])
		self.image = ascii_mandalorian
		self.vsp = VER_SPEED
		self.hsp = HOR_SPEED
		self.name = "mandalorian"

	def move_right(self):
		if self.y+self.hsp<self.c:
			self.y+=self.hsp

	def move_left(self):
		if self.y-self.hsp>=0:
			self.y-=self.hsp

	def move_down(self):
		if self.x+self.vsp+4<self.r:
			self.x+=self.vsp

	def move_up(self):
		if self.x-self.vsp>4:
			self.x-=self.vsp

	def check_char(self,x):
		if x=='w':
			self.move_up()
		elif x=='s':
			self.move_down()
		elif x=='a':
			self.move_left()
		elif x=='d':
			self.move_right()