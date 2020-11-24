class Date:
	def __init__(self,month,day,year):
		self.month = month
		self.day = day
		self.year = year


	def getmonth(self):
		return self.month
	def setmonth(self,month):
		self.month = month

	def getday(self):
		return self.day

	def setdate(self,day):
		self.day = day

	def getyear(self):
		return self.year

	def setyear():
		self.year = year


	def setday(self,day):
                self.day = day

	def print_method1_1(self):
	#return self.month +' '+self.


class Movie:
	def __init__(self,movie,director,genre,IMDB):
		self.movie= movie
		self.director = director
		self.genre = genre
		self.IMDB = IMDB

	def setmovie(self,movie):
		self.movie= movie
	def setdirector(self,director):
		self.director= director

	def setgenre(self,genre):
		self.genre = genre

	def setIMDB(self,IMDB):
		self.IMDB = IMDB

	def getmovie(self):
		return self.movie
	def getdirector(self):
		return self.director

	def getgenre(self):
		return self.genre
	def getIMDB(self):
		return self.IMDB

movie_1 = Movie("dabang","salman","action",5.0)
movie_2 = Movie("laila","sunny","romance",2.1)
movie_3 = Movie("perfect","who","comedy",9.7)
movie_4 = Movie("coco","pixar","musical",10)
movie_5 = Movie("amma","satayjeet","b/w",6.4)

#for i in range(5):
#	lowest = movie_1


def area(r):
	area = (r**2)*pi
	return area

print(area(1))
