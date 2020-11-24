class Employee:
	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		return self.pay

	def __repr__(self):
		pass

	def __str__(self):
		pass
		

class Developer(Employee):
	def __init__(self,first,last,pay,prog_lang):
		
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

	raise_amount = 1.10
	pass

class Manager(Employee):

	def __init__(self,first,last,pay,employees = None):
		super().__init__(first,last,pay)
		if employees == 'None':
			self.employees = []

		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('----->',emp.fullname)


emp_1 = Employee('harshal','dev',1000)

emp_2 = Employee('test','user',200)


dev_1 = Developer('Dev','harshal',50000,'python')
dev_2 = Developer("dholchike","",10,'java')


mgr_1 = Manager('sue','smith',90000,[dev_1])







#print(emp_2.email)
#print(emp_1.email)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(emp_1.raise_amount)
#emp_1.raise_amount = 5
#print(emp_1.raise_amount)
#print(emp_1.apply_raise())
#print(Employee.num_of_emps)



#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_2.fullname())

#print(dev_1.email)
#print(dev_1.prog_lang)


#print(mgr_1.print_emps())
#mgr_1.add_emp(dev_2)
#print(mgr_1.print_emps())
#mgr_1.remove_emp(dev_1)
#print(mgr_1.print_emps())
