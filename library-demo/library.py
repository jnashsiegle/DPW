class FavoriteMovies(object):
	def __init__(self):
		self.__movie_list = []
		pass
		#To Do List -
		#have an array to hold the movie info
		#have some way to add to above array
		#generate a list of movies at the end
		#calculate time span between movies

	def add_movie(self, m):
		self.__movie_list.append(m)
		print m.title #prints out title when lib.addMovie(mdx) attribute is attached to movie

	def compile_list(self):
		output = ''
		for movie in self.__movie_list: # for each movie in movie array 
			output += 'Title: ' + movie.title + ' (' + str(movie.year) + ') Directed by: ' + movie.director + '<br />'
		return output

	def calc_time_span(self):
		'''
		calculate the time in between movies
		'''
		#years
		years = []
		for movie in self.__movie_list:
			years.append(movie.year)
		#print years #test to see if the above works
		#sort years from low to high
		years.sort()
		print years
		#subtract the low year from the high year
		num = len(years) - 1 #0 based this gives us total length minus the 1 for 0 based indexing
		span = years[num] - years [0] # last number - first number
		return 'The span between films entered is ' +  str(span)
		#return the span of time

class MovieData(object): # Data Object
	def __init__(self):
		self.title = ''
		self.__year = 0 #for assignment make sure to check for valid year
		self.director = ''
		#

	@property
	def year(self):
	    return self.__year

	@year.setter
	def year(self, y):
		if y > 2014: #perform a validity check
			print "Error, invalid date!"
		else:
			self.__year = y

	