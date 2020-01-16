from config import *
from ascii_stuff import *
import numpy

class Person:

	def __init__(self):
		self._r = ROWS
		self._c = COLUMNS
		self._offset = 0
		self._x = 0
		self._y = 0
		self._name = ""

class Enemy(Person):

	def enemy_init(self,x,y):
		self.__x = x
		self.__y = y
		self.__rows = len(ascii_enemy)
		self.__columns = len(ascii_enemy[0])
		self.__image = ascii_enemy
		self.__vsp = 0
		self.__hsp = ENEMY_SPEED
		self.__name = "enemy"
		self.__delete = 0
		self.__priority = priorities["enemy"]

	def move(self):
		self.__y -= self.__hsp
		if self.__y == -10:
			self.__delete = 1

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self.__rows):
			for k in range(self.__columns):
				if self.__x+j>=0 and self.__x+j<obj.get_r() and self.__y+k>=0 and self.__y+k<obj.get_c() and self.__image[j][k]!=' ':
					if arr[self.__x+j][self.__y+k]==1:
						return 1
		return 0

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_r(self):
		return self._r

	def get_c(self):
		return self._c

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1

class Jet_Boy(Person):

	def jb_init(self):
		self.__x = 29
		self.__y = 10
		self.__rows = len(ascii_mandalorian)
		self.__columns = len(ascii_mandalorian[0])
		self.__image = ascii_mandalorian
		self.__vsp = VER_SPEED
		self.__hsp = HOR_SPEED
		self.__name = "mandalorian"
		self.__hurt = 1
		self.__fr = FRAME_RATE
		self.__shoot_time = SHOOT_TIME
		self.__can_shoot = 0
		self.__priority = priorities["mandalorian"]

	def move_right(self):
		if self.__y+self.__hsp<self._c:
			self.__y+=self.__hsp

	def move_left(self):
		if self.__y-self.__hsp>=0:
			self.__y-=self.__hsp

	def move_down(self):
		if self.__x+self.__vsp+4<self._r:
			self.__x+=self.__vsp

	def move_up(self):
		if self.__x-self.__vsp>4:
			self.__x-=self.__vsp

	def shoot(self,arr):
		if self.__can_shoot == 0:
			arr.append(ball(self.__x,self.__y+5))
			self.__can_shoot += (self.__fr*self.__shoot_time)

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

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_can_shoot(self):
		return self.__can_shoot

	def dec_shoot(self):
		self.__can_shoot -= 1

	def get_name(self):
		return self.__name

	def get_r(self):
		return self._r

	def get_c(self):
		return self._c

class Cloud:

	def __init__(self,x,y):
		self.__rows = len(ascii_cloud)
		self.__columns = len(ascii_cloud[0])
		self.__image = ascii_cloud
		self.__x = x
		self.__y = y
		self.__delete = 0
		self.__name = "cloud"

	def move(self):
		self.__y -= 1
		if self.__y == -10:
			self.__delete = 1

class Parent:

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self.get_rows()):
			for k in range(self.get_columns()):
				if self.get_x()+j>=0 and self.get_x()+j<obj.get_r() and self.get_y()+k>=0 and self.get_y()+k<obj.get_c() and self.get_image()[j][k]!=' ':
					if arr[self.get_x()+j][self.get_y()+k]==1:
						return 1
		return 0

class Coin(Parent):

	def __init__(self,x,y):
		self.__rows = len(ascii_coin)
		self.__columns = len(ascii_coin[0])
		self.__image = ascii_coin
		self.__x = x
		self.__y = y
		self.__delete = 0
		self.__name = "coin"
		self.__priority = priorities["coin"]

	def move_magnet(self,x):
		if self.__y < x.get_y():
			self.move()
		else:
			if self.__x < x.get_x():
				if x.get_x() - self.__x > self.__y - x.get_y():
					self.__x += 1
				else:
					self.__y -= 1
			else:
				if self.__x - x.get_x() > self.__y - x.get_y():
					self.__x -= 1
				else:
					self.__y -= 1
	def move(self):
		self.__y -= 1
		if self.__y == -10:
			self.__delete = 1

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1

class Bars(Parent):

	def __init__(self,x,y,p):
		self.__rows = len(ascii_bars[p])
		self.__columns = len(ascii_bars[p][0])
		self.__image = ascii_bars[p]
		self.__x = x
		self.__y = y
		self.__delete = 0
		self.__name = "bar"
		self.__priority = priorities["bar"]

	def move(self):
		self.__y -= 1
		if self.__y == -10:
			self.__delete = 1

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1

class ball:

	def __init__(self,x,y):
		self.__rows = len(ascii_ball)
		self.__columns = len(ascii_ball[0])
		self.__r = ROWS
		self.__c = COLUMNS
		self.__image = ascii_ball
		self.__x = x
		self.__y = y
		self.__delete = 0
		self.__name = "ball"
		self.__ball_speed = BALL_SPEED
		self.__priority = priorities["ball"]

	def move(self):
		self.__y += self.__ball_speed
		if self.__y>120:
			self.__delete = 1

	def chk(self,obj):
		arr = []
		for i in range(self.__r):
			arr.append([0]*self.__c)

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<self.__c and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self.__rows):
			for k in range(self.__columns):
				if self.__x+j>=0 and self.__x+j<self.__r and self.__y+k>=0 and self.__y+k<self.__c and self.__image[j][k]!=' ':
					if arr[self.__x+j][self.__y+k]==1:
						return 1
		return 0

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_r(self):
		return self.__r

	def get_c(self):
		return self.__c

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1

class Parent2:

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self.get_rows()):
			for k in range(self.get_columns()):
				if self.get_x()+j>=0 and self.get_x()+j<obj.get_r() and self.get_y()+k>=0 and self.get_y()+k<obj.get_c() and self.get_image()[j][k]!=' ':
					if arr[self.get_x()+j][self.get_y()+k]==1:
						self._delete = 1
						return 1
		return 0

class Magnet(Parent2):

	def __init__(self,x,y):
		self.__rows = len(ascii_magnet)
		self.__columns = len(ascii_magnet[0])
		self.__image = ascii_magnet
		self.__x = x
		self.__y = y
		self._delete = 0
		self.__name = "magnet"
		self.__dir = 1
		self.__priority = priorities["magnet"]

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def move(self):
		self.__y -= 1
		if self.__y == -10:
			self._delete = 1

		if self.__dir:
			self.__x += 1
			if self.__x == 25:
				self.__dir = 0
		else:
			self.__x -= 1
			if self.__x == 10:
				self.__dir = 1

	def get_delete(self):
		return self._delete

	def delt(self):
		self._delete = 1

class Boost(Parent2):

	def __init__(self,x,y):
		self.__rows = len(ascii_boost)
		self.__columns = len(ascii_boost[0])
		self.__image = ascii_boost
		self.__x = x
		self.__y = y
		self._delete = 0
		self.__name = "boost"
		self.__dir = 1
		self.__priority = priorities["boost"]

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def move(self):
		self.__y -= 1
		if self.__y == -10:
			self._delete = 1

		if self.__dir:
			self.__x += 1
			if self.__x == 25:
				self.__dir = 0
		else:
			self.__x -= 1
			if self.__x == 10:
				self.__dir = 1

	def get_delete(self):
		return self._delete

	def delt(self):
		self._delete = 1

class Shield:

	def __init__(self):
		self.__rows = len(ascii_shield)
		self.__columns = len(ascii_shield[0])
		self.__image = ascii_shield
		self.__x = 0
		self.__y = 0
		self.__delete = 0
		self.__name = "shield"
		self.__priority = priorities["shield"]
		self.__shield_time = SHIELD_TIME*FRAME_RATE

	def move(self):
		pass

	def update_shield(self,x,y):
		self.__x = x
		self.__y = y
		if self.__shield_time > 0:
			self.__shield_time -= 1
			return 1
		self.__delete = 1
		return 0

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1

class Dragon:

	def __init__(self,x,y):
		self.__rows = len(ascii_dragon)
		self.__columns = len(ascii_dragon[0])
		self.__image = ascii_dragon
		self.__x = x
		self.__y = y
		self.__delete = 0
		self.__name = "dragon"
		self.__priority = priorities["dragon"]

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self.__rows):
			for k in range(self.__columns):
				if self.__x+j>=0 and self.__x+j<obj.get_r() and self.__y+k>=0 and self.__y+k<obj.get_c() and self.__image[j][k]!=' ':
					if arr[self.__x+j][self.__y+k]==1:
						return 1
		return 0

	def move(self,x):
		pass

	def move_dragon(self,x):

		if self.__x + 7 > x.x and self.__x > 1:
			self.__x -= 1
			return 1

		if self.__x + 7 < x.x and self.__x < 19:
			self.__x += 1
			return 1

		return 0

	def get_priority(self):
		return self.__priority

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_image(self):
		return self.__image

	def get_name(self):
		return self.__name

	def get_delete(self):
		return self.__delete

	def delt(self):
		self.__delete = 1