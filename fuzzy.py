from operator import add, mul, div, sub
import shapely

class NombreFlou(object):

	def __init__(self, xcoord, ycoord = [0, 1, 1, 0]):
		self.xcoord = self.make_coord(xcoord)
		self.ycoord = self.make_coord(ycoord)



	def make_coord(self, data):
		if isinstance(data, int):
			data = list(data)			
		if len(data) == 1:
			data = data*4
		elif len(data) == 2:
			data = data[:1]*2 + data[1:]*2
		elif len(data) == 3:
			data = data[:1]+ data[1:2]*2 + data[2:]
		return data

	def check_nf(self, nf):
		if isinstance(nf, NombreFlou):
			return(nf)
		else:
			return(NombreFlou(self.check_data(nf)))

	def __add__(self, nf):
		nf = check_nf(nf)
		return NombreFlou(map(add, self.xcoord, nf.xcoord))

	def __sub__(self, nf):
		nf = check_nf(nf)
		return NombreFlou(map(sub, self.xcoord, nf.xcoord))

	def __mul__(self, nf):
		nf = check_nf(nf)
		return NombreFlou(map(mul, self.xcoord, nf.xcoord))

	def __div__(self, nf):
		nf = check_nf(nf)
		return NombreFlou(map(div, self.xcoord, nf.xcoord.reverse()))

	def intersect(self, nf):
		for i in range(0, 3):
			if (self.xcoord(i) != self.self.xcoord(i+1)) and (self.ycoord(i) != self.self.ycoord(i+1)):
				pass

 
