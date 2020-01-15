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

class Enemy(Person):

	def enemy_init(self,x,y):
		self.x = x
		self.y = y
		self.rows = len(ascii_enemy)
		self.columns = len(ascii_enemy[0])
		self.image = ascii_enemy
		self.vsp = 0
		self.hsp = ENEMY_SPEED
		self.name = "enemy"
		self.delete = 0
		self.priority = priorities["enemy"]

	def move(self):
		self.y -= self.hsp
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
		self.hurt = 1
		self.fr = FRAME_RATE
		self.shoot_time = SHOOT_TIME
		self.can_shoot = 0
		self.priority = priorities["mandalorian"]

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

	def shoot(self,arr):
		if self.can_shoot == 0:
			arr.append(ball(self.x,self.y+5))
			self.can_shoot += (self.fr*self.shoot_time)

	def add_shield(self,arr):
		arr.append(Shield())

	def check_char(self,x,arr):
		if x=='w':
			self.move_up()
		elif x==' ':
			self.add_shield(arr)
		elif x=='s':
			self.move_down()
		elif x=='a':
			self.move_left()
		elif x=='d':
			self.move_right()
		elif x=='l':
			self.shoot(arr)
		elif x=='Q':
			exit()

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
		self.priority = priorities["coin"]

	def move_magnet(self,x):
		if self.y < x.y:
			self.move()
		else:
			if self.x < x.x:
				if x.x - self.x > self.y - x.y:
					self.x += 1
				else:
					self.y -= 1
			else:
				if self.x - x.x > self.y - x.y:
					self.x -= 1
				else:
					self.y -= 1

class Bars(Parent):

	def __init__(self,x,y,p):
		self.rows = len(ascii_bars[p])
		self.columns = len(ascii_bars[p][0])
		self.image = ascii_bars[p]
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "bar"
		self.priority = priorities["bar"]

class ball:

	def __init__(self,x,y):
		self.rows = len(ascii_ball)
		self.columns = len(ascii_ball[0])
		self.r = ROWS
		self.c = COLUMNS
		self.image = ascii_ball
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "ball"
		self.ball_speed = BALL_SPEED
		self.priority = priorities["ball"]

	def move(self):
		self.y += self.ball_speed
		if self.y>120:
			self.delete = 1

	def chk(self,obj):
		arr = []
		for i in range(self.r):
			arr.append([0]*self.c)

		for j in range(obj.rows):
			for k in range(obj.columns):
				if obj.y+k>=0 and obj.y+k<self.c and obj.image[j][k]!=' ':
					arr[obj.x+j][obj.y+k] = 1

		for j in range(self.rows):
			for k in range(self.columns):
				if self.x+j>=0 and self.x+j<self.r and self.y+k>=0 and self.y+k<self.c and self.image[j][k]!=' ':
					if arr[self.x+j][self.y+k]==1:
						return 1

		return 0

class Parent2:

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
						self.delete = 1
						return 1
		return 0

	def move(self):
		self.y -= 1
		if self.y == -10:
			self.delete = 1

		if self.dir:
			self.x += 1
			if self.x == 25:
				self.dir = 0
		else:
			self.x -= 1
			if self.x == 10:
				self.dir = 1

class Magnet(Parent2):

	def __init__(self,x,y):
		self.rows = len(ascii_magnet)
		self.columns = len(ascii_magnet[0])
		self.image = ascii_magnet
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "magnet"
		self.dir = 1
		self.priority = priorities["magnet"]

class Boost(Parent2):

	def __init__(self,x,y):
		self.rows = len(ascii_boost)
		self.columns = len(ascii_boost[0])
		self.image = ascii_boost
		self.x = x
		self.y = y
		self.delete = 0
		self.name = "boost"
		self.dir = 1
		self.priority = priorities["boost"]

class Shield:

	def __init__(self):
		self.rows = len(ascii_shield)
		self.columns = len(ascii_shield[0])
		self.image = ascii_shield
		self.x = 0
		self.y = 0
		self.delete = 0
		self.name = "shield"
		self.priority = priorities["shield"]
		self.shield_time = SHIELD_TIME*FRAME_RATE

	def move(self):
		pass

	def update_shield(self,x,y):
		self.x = x
		self.y = y
		if self.shield_time > 0:
			self.shield_time -= 1
			return 1
		self.delete = 1
		return 0