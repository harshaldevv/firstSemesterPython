class Point:
	def __init__(self,x,y,z):
		self.x = x 
		self.y = y
		self.z = z

	pass

class Student:
	"""Details about the college student"""
	max_credit = 22
	def __init__(self,netID,courses= [],major=None):
		assert type(netID) ==str,"netID should be of type str"
		assert type(courses) ==list,"courses should be in a list"
		assert type(major) == str , "major , if taken, should be a 'str'"


		self.netID = netID
		self.courses = courses
		self._major = major

	def getmajor(self):
		if self._major == None:
			return ""

		return self._major

	def setmajor(self,m):
		self._major = m
		pass

class shape:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def draw(self):
		pass

class circle(shape):
	def __init__(self,x,y,radius):
		super().__init__(x,y)
		self.radius = radius
	
	def draw(self):
		return "drawing circle"
		


c1 = circle(0,0,4)
r = c1.radius
print(r)
print(c1.draw())



class Employee:
	num_of_emp = 0
	def __init__(self,first,last,age,):
		self.first = first
		self.last = last
		self.age = age
		self.email = first+'.'+last + '@company.com'
		self.num_of_emp +=1

class Developer(Employee):
	def __init__(self,first,last,age,prog_lang):
		super().__init__(first,last,age)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self,fist,last,age,em = None):
		super().__init__(first,last,age)
		if em == None:
			self.em = []

		else:
			self.em = em

	def add_em(self,emp):
		self.emp = emp
		if emp not in em:
			em.append(emp)

	def remove_emp(self,emp):
		self.emp = emp
		if emp in em:
			em.remove(emp)


        #def print_emp(self):
         #       for emp in em:
          #              print(emp)

	
emp_1 = Employee('harshal','dev','20')
emp_2 = Employee('dholchike','','25')
print(emp_1.email)

def fib(n):
	fib = [1,1]
	for i in range(2,n):
		fib.append(fib[-1]+fib[-2])

	return fib

print(fib(5))

k = 0
sum = 0
#while k<10:
#	num = int(input())
#	sum+=num

#	k+=1
#print(sum/10)


def swap(x,y):
	x = x+y
	y = x-y
	x = x-y
	return(x,y)

print(swap(3,5))


def fix_teen(n):
	list = [13,14,17,18]
	if n in list:
		n=0
	else:
		n=n
	return n 

def no_teen_sum(a,b,c):
	a = fix_teen(a)
	b = fix_teen(b)
	c = fix_teen(c)

	return (a+b+c)
	

print(no_teen_sum(4,14,5))

def grade(n):
	if n >91 and n<101:
		return "A"

	elif n >76 and n <91:
		return "B"

	elif n>61 and n<76:
		return "C"

	elif n >46 and n<61:
		return "D"

	elif n>=0 and n <=45:
		return "F"

print(grade(95))

print(grade(77))

print(grade(60))


print(grade(55))

print(grade(40))

def solve(S, K):
	if (K%3 == 0 or K%5 == 0) and K%15 != 0:
		P = K
	else:
		P = 0
	return S + S*P

print(solve("ab",1))

def sign(a,b):
	if a*b>0:
		return "same sign"

	elif a*b <0:
		return "oppo sign"
	else:
		return "one of them is zero"

print(sign(0,5))
print(sign(1,4,))
print(sign(1,-2))


def change_date(Date,year_fix):
	assert type(Date)==str,"Date should be in string"
	assert type(year_fix)==int, "year_fix should be an int"

	date = Date[3:5]
	month = Date[:2]
	year = (Date[6:])

	
	return date+"-"+month+"-"+ str(int(year)+year_fix) 

print(change_date("04 22 2000",5))


def num_print(n):
	for i in range(1,n+1):
		print (i)

print(num_print(5))


i = int(input("enter the number"))
for i in range(1,i+1):
	print ('*' * (i))


import random
a = []
for i in range(30):
	a.append(random.randint(0,1000))

print(a)

for i in range(len(a)):
	for j in range(i):
		if a[j]>a[i]:
			a[j],a[i]=a[i],a[j]
	#	print("step wise sorted list ",a)


print('sorted list is ' ,a)













