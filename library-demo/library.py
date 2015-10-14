class FavoriteMovies(object):
	def __init__(self):
		self.__movie_list = []
		pass
		#To Do List -
		#have an array to hold the movie info
		#have some way to add to above array
		#generate a list of movies at the end
		#calculate time span between movies

	def addMovie(self, m):
		self.__movie_list.append(m)
		print m.title




class MovieData(object): # Data Object
	def __init__(self):
		self.title = ''
		self.__year = 0 #for assignment make sure to check for valid year
		self.director = ''
		#

	@property
	def year(self):
	    pass

	@year.setter
	def year(self, y):
		if y > 2014: #perform a validity check
			print "Error, invalid date!"
		else:
			self.__year = y

	