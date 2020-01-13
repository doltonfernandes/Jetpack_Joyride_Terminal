import numpy
from config import *
from ascii_stuff import *

class Cloud:

	def __init__(self,a):
		self.rows = ROWS
		self.columns = COLUMNS + 20
		self.image = numpy.array([[" "]*self.columns])
		for i in range(self.rows-1):
			self.image = numpy.vstack([self.image,[' ']*self.columns])
		self.offset = 0
		for i in range(len(ascii_cloud)):
			for j in range(len(ascii_cloud[i])):
				self.image[a+i][self.columns-15+j] = ascii_cloud[i][j]