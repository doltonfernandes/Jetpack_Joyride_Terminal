from os import system
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

class Parent_Func:

	def get_priority(self):
		return self._priority

	def get_x(self):
		return self._x

	def get_y(self):
		return self._y

	def get_rows(self):
		return self._rows

	def get_columns(self):
		return self._columns

	def get_image(self):
		return self._image

	def get_name(self):
		return self._name

	def get_r(self):
		return self._r

	def get_c(self):
		return self._c

	def get_delete(self):
		return self._delete

	def delt(self):
		self._delete = 1

class Enemy(Person,Parent_Func):

	def enemy_init(self,x,y):
		self._x = x
		self._y = y
		self._rows = len(ascii_enemy)
		self._columns = len(ascii_enemy[0])
		self._image = ascii_enemy
		self.__vsp = 0
		self.__hsp = ENEMY_SPEED
		self._name = "enemy"
		self._delete = 0
		self._priority = priorities["enemy"]

	def move(self):
		self._y -= self.__hsp
		if self._y <= -10:
			self._delete = 1

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self._rows):
			for k in range(self._columns):
				if self._x+j>=0 and self._x+j<obj.get_r() and self._y+k>=0 and self._y+k<obj.get_c() and self._image[j][k]!=' ':
					if arr[self._x+j][self._y+k]==1:
						return 1
		return 0

class Jet_Boy(Person,Parent_Func):

	def jb_init(self):
		self._x = 40
		self._y = 10
		self._rows = len(ascii_mandalorian)
		self._columns = len(ascii_mandalorian[0])
		self._image = ascii_mandalorian
		self.__vsp = VER_SPEED
		self.__hsp = HOR_SPEED
		self.__uplast = TIME
		self.__interval1 = 0
		self.__interval2 = 0
		self._name = "mandalorian"
		self.__hurt = 1
		self.__fr = FRAME_RATE
		self.__shoot_time = SHOOT_TIME
		self.__can_shoot = 0
		self._priority = priorities["mandalorian"]
		self.__shield_time = 0
		self.__par = 0

	def move_right(self):
		if self._y+self.__hsp<self._c:
			self._y+=self.__hsp

	def move_left(self):
		if self._y-self.__hsp>=0:
			self._y-=self.__hsp

	def move_down(self,t):
		if self.__uplast - t <= 1:
			self.__interval2 = 0
			return 0
		if self.__interval2 < 10:
			self.__interval2 += 0.3
		if self._x+self.__vsp+int(self.__interval2)+9<self._r:
			self._x+=self.__vsp+int(self.__interval2)
		else:
			self._x = 40 - self.__par
		return 1

	def move_up(self):
		if self._x-self.__vsp-self.__interval1>4:
			self._x-=self.__vsp + int(self.__interval1)
		else:
			self._x = 6

	def shoot(self,arr):
		if self.__can_shoot == 0:
			arr.append(ball(self._x+1,self._y+5))
			self.__can_shoot += (self.__fr*self.__shoot_time)

	def add_shield(self,arr,t):
		if arr[0].__shield_time >= 60:
			arr.append(Shield(t))

	def check_char(self,neckarr,x,arr,t):
		if x=='w':
			self.__interval2 = 0
			if self.__uplast - t > 1:
				self.__uplast = t
				self.__interval1 = 0
			else:
				self.__interval1 += 0.6
			self.move_up()
		elif x==' ':
			self.add_shield(arr,t)
		elif x=='a':
			self.move_left()
		elif x=='d':
			self.move_right()
		elif x=='l':
			self.shoot(arr)
		elif x=='0':
			self.switch_to(1)
			for i in range(20):
				neckarr.append(Dragon_neck(self._x,self._y))
		elif x=='Q':
			system("stty echo");
			system("killall mpg123")
			exit()

	def get_can_shoot(self):
		return self.__can_shoot

	def dec_shoot(self):
		self.__can_shoot -= 1

	def get_shield_time(self):
		return self.__shield_time

	def update_shield_time(self):
		if self.__shield_time < 60:
			self.__shield_time += 1

	def reset_shield_time(self):
		self.__shield_time = 0

	def switch_to(self,x):
		if x:
			self._rows = len(ascii_dragon_head)
			self._columns = len(ascii_dragon_head[0])
			self._image = ascii_dragon_head
			self.__par = 2
		else:
			self._rows = len(ascii_mandalorian)
			self._columns = len(ascii_mandalorian[0])
			self._image = ascii_mandalorian
			self.__par = 0

class Cloud:

	def __init__(self,x,y):
		self._rows = len(ascii_cloud)
		self._columns = len(ascii_cloud[0])
		self._image = ascii_cloud
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "cloud"

	def move(self):
		self._y -= 1
		if self._y <= -10:
			self._delete = 1

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

class Coin(Parent,Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_coin)
		self._columns = len(ascii_coin[0])
		self._image = ascii_coin
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "coin"
		self._priority = priorities["coin"]

	def move_magnet(self,x):
		if self._y < x.get_y():
			self.move()
		else:
			if self._x < x.get_x():
				if x.get_x() - self._x > self._y - x.get_y():
					self._x += 1
				else:
					self._y -= 1
			else:
				if self._x - x.get_x() > self._y - x.get_y():
					self._x -= 1
				else:
					self._y -= 1
	def move(self):
		self._y -= 1
		if self._y <= -10:
			self._delete = 1

class Bars(Parent,Parent_Func):

	def __init__(self,x,y,p):
		self._rows = len(ascii_bars[p])
		self._columns = len(ascii_bars[p][0])
		self._image = ascii_bars[p]
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "bar"
		self._priority = priorities["bar"]

	def move(self):
		self._y -= 1
		if self._y == -20:
			self._delete = 1

class ball(Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_ball)
		self._columns = len(ascii_ball[0])
		self.__r = ROWS
		self.__c = COLUMNS
		self._image = ascii_ball
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "ball"
		self.__ball_speed = BALL_SPEED
		self._priority = priorities["ball"]

	def move(self):
		self._y += self.__ball_speed
		if self._y > 200:
			self._delete = 1

	def chk(self,obj):
		arr = []
		for i in range(self.__r):
			arr.append([0]*self.__c)

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<self.__c and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self._rows):
			for k in range(self._columns):
				if self._x+j>=0 and self._x+j<self.__r and self._y+k>=0 and self._y+k<self.__c and self._image[j][k]!=' ':
					if arr[self._x+j][self._y+k]==1:
						return 1
		return 0

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

class Magnet(Parent2,Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_magnet)
		self._columns = len(ascii_magnet[0])
		self._image = ascii_magnet
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "magnet"
		self.__dir = 1
		self._priority = priorities["magnet"]

	def move(self):
		self._y -= 1
		if self._y <= -10:
			self._delete = 1

		if self.__dir:
			self._x += 1
			if self._x >= 25:
				self.__dir = 0
		else:
			self._x -= 1
			if self._x <= 10:
				self.__dir = 1

class Boost(Parent2,Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_boost)
		self._columns = len(ascii_boost[0])
		self._image = ascii_boost
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "boost"
		self.__dir = 1
		self._priority = priorities["boost"]

	def move(self):
		self._y -= 1
		if self._y <= -10:
			self._delete = 1

		if self.__dir:
			self._x += 1
			if self._x >= 25:
				self.__dir = 0
		else:
			self._x -= 1
			if self._x <= 10:
				self.__dir = 1

class Shield(Parent_Func):

	def __init__(self,x):
		self._rows = len(ascii_shield)
		self._columns = len(ascii_shield[0])
		self._image = ascii_shield
		self._x = 0
		self._y = 0
		self._delete = 0
		self._name = "shield"
		self._priority = priorities["shield"]
		self.__shield_ini_time = x
		self.__shield_time = SHIELD_TIME

	def move(self):
		pass

	def update_shield(self,x,y,t):
		self._x = x
		self._y = y
		if self.__shield_ini_time - self.__shield_time > t:
			self._delete = 1
			return 0
		return 1

	def get_shield_ini_time(self):
		return self.__shield_ini_time

	def get_shield_time(self):
		return self.__shield_time

class Dragon(Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_dragon)
		self._columns = len(ascii_dragon[0])
		self._image = ascii_dragon
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "dragon"
		self._priority = priorities["dragon"]
		self.__dragon_time = DRAG_TIME
		self.__dragt = DRAG_TIME
		self.__lives = DRAGON_LIVES

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self._rows):
			for k in range(self._columns):
				if self._x+j>=0 and self._x+j<obj.get_r() and self._y+k>=0 and self._y+k<obj.get_c() and self._image[j][k]!=' ':
					if arr[self._x+j][self._y+k]==1:
						return 1
		return 0

	def move(self,x):
		pass

	def move_dragon(self,x,arr):
		self.__dragon_time -= 1
		if self.__dragon_time == 0:
			arr.append(Ice_ball(self._x + 9,self._y - 1))
			self.__dragon_time = self.__dragt
		if self._x + 7 > x.get_x() and self._x > 1:
			self._x -= 1
			return 1

		if self._x + 7 < x.get_x() and self._x < 30:
			self._x += 1
			return 1

		return 0

	def get_lives(self):
		return self.__lives

	def dec_lives(self):
		self.__lives -= 1

class Magnet_Assignment(Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_magnet2)
		self._columns = len(ascii_magnet2[0])
		self._image = ascii_magnet2
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "magnet2"
		self._priority = priorities["magnet2"]
		self.__force = 5
		self.__cnt = 0

	def chk(self,obj):
		arr = []
		for i in range(obj.get_r()):
			arr.append([0]*obj.get_c())

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<obj.get_c() and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self._rows):
			for k in range(self._columns):
				if self._x+j>=0 and self._x+j<obj.get_r() and self._y+k>=0 and self._y+k<obj.get_c() and self._image[j][k]!=' ':
					if arr[self._x+j][self._y+k]==1:
						return 1
		return 0

	def move(self,x,t):
		self.move_mand_magnet(x,t)
		self.__cnt += 1
		self._y -= 1
		if self._y <= -10:
			self._delete = 1

	def move_mand_magnet(self,x,t):
		if self.__cnt % self.__force != 0:
			return 0
		a = x.get_x() - self._x
		b = x.get_y() - self._y
		if b > 0:
			x.move_left()
		else:
			x.move_right()
		if a > 0:
			x.move_up()
		else:
			x.move_down(t)
		return 1

class Ice_ball(Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_ice_ball)
		self._columns = len(ascii_ice_ball[0])
		self.__r = ROWS
		self.__c = COLUMNS
		self._image = ascii_ice_ball
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "ice_ball"
		self.__ball_speed = ICE_BALL_SPEED
		self._priority = priorities["ice_ball"]

	def move(self):
		self._y -= self.__ball_speed
		if self._y <= -10:
			self._delete = 1

	def chk(self,obj):
		arr = []
		for i in range(self.__r):
			arr.append([0]*self.__c)

		for j in range(obj.get_rows()):
			for k in range(obj.get_columns()):
				if obj.get_y()+k>=0 and obj.get_y()+k<self.__c and obj.get_image()[j][k]!=' ':
					arr[obj.get_x()+j][obj.get_y()+k] = 1

		for j in range(self._rows):
			for k in range(self._columns):
				if self._x+j>=0 and self._x+j<self.__r and self._y+k>=0 and self._y+k<self.__c and self._image[j][k]!=' ':
					if arr[self._x+j][self._y+k]==1:
						return 1
		return 0

class Dragon_neck(Parent2,Parent_Func):

	def __init__(self,x,y):
		self._rows = len(ascii_dragon_neck)
		self._columns = len(ascii_dragon_neck[0])
		self._r = ROWS
		self._c = COLUMNS
		self._image = ascii_dragon_neck
		self._x = x
		self._y = y
		self._delete = 0
		self._name = "neck"
		self._priority = priorities["neck"]
		self.__deque = []
		self.__lim = 100

	def move(self,x,y):
		if x > self._x:
			self._x += min(4,x-self._x)
		elif x < self._x:
			self._x -= min(4,self._x-x)
		if y > self._y:
			self._y += min(4,y-self._y)
		elif y < self._y:
			self._y -= min(4,self._y-y)

	def app(self,x,y):
		if len(self.__deque) == self.__lim:
			self.__deque.pop(0)
		self.__deque.append([x,y])

	def get_deque(self):
		return self.__deque