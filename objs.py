from config import *
import numpy

class Person:

	def __init__(self):
		self.rows = ROWS
		self.columns = COLUMNS
		self.offset = 0
		self.x = 30
		self.y = 10

class Jet_Boy(Person):

	def jb_init(self):
		self.vsp = VER_SPEED
		self.hsp = HOR_SPEED

	def move_right(self):
		if self.y+self.hsp<self.columns:
			self.y+=self.hsp

	def move_left(self):
		if self.y-self.hsp>=0:
			self.y-=self.hsp

	def move_down(self):
		if self.x+self.vsp+4<self.rows:
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