

class movie:
	def __init__(self,title,director,genre,IMDB):
		self.title = title
		self.director = director
		self.genre = genre
		self.IMDB = IMDB

	def gettitle(self):
		return self.title

	def settitle(self,title):
		self.title = title

	def getdirector(self):
		return self.director

	def setdirector(self,director):
		self.director=director
	

	def getgenre(self):
		return self.genre

	def setgenre(self,genre):
		self.genre = genre

	def getIMDB(self):
		return self.IMDB

	def setIMDB(self,IMDB):
		self.IMDB=IMDB
	def __str__(self):
		return self.title
		

    
m1 = movie("body","salman","action",0.0)
m2 = movie("date","noah","romantic",5.0)
m3 = movie("five feet","srk","romcom",8.0)
m4 = movie("friends","duh","romcom",9.7)
m5 = movie("Ra1","gauri","action",7.7)

x = [m1,m2,m3,m4,m5]
print(m1)

def compare(m):
	return m.IMDB

x = sorted(x,key = compare)

for i in x:
    print(x)


class Geek: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
  
raj = Geek() 
  
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
print(raj.get_age()) 
  
print(raj._age)


#__add__
class Day(object):
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts

    def __add__(self, other):
        total_visits = self.visits + other.visits
        total_contacts = self.contacts + other.contacts
        return Day(total_visits, total_contacts)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self):
        return "Visits: %i, Contacts: %i" % (self.visits, self.contacts)

day1 = Day(10, 1)
day2 = Day(20, 2)
print (day1)
# Visits: 10, Contacts: 1
print day2
# Visits: 20, Contacts: 2

day3 = day1 + day2
print day3
# Visits: 30, Contacts: 3

day4 = sum([day1, day2, day3])
print day4
# Visits: 60, Contacts: 6
