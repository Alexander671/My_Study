class Person:
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		self.name = self.name.split()[-1]
	def getRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))
	def __repr__ (self) :
		# Добавленный метод
		return '[Person: %s, %s]' % (self.name, self .pay) # Строка для вывода

class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)
	def getRaise(self, percent, bonus=0.10):
		Person.getRaise(self, percent + bonus)

class Department:
	def __init__ (self, *args):
		self.members = list(args)
	def addMember(self, person):
		self.members .append(person)
	def giveRaises(self, percent):
		for person in self.members:
			person.getRaise(percent)
	def showAll(self):
		for person in self.members:
			print(person)


if __name__ == "__main__" :
	# Только когда запускается для тестирования
	# Код самотестирования
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job="dev", pay=100000)
	print(bob)
	print(bob.name, bob.pay)
	print(sue.name, sue.pay)
	bob.lastName()
	print(bob.name)
	sue.getRaise(0.1)
	print(sue.pay)
	alex = Manager('Alex Smith', pay=100000)
	alex.getRaise(0.10, 0.10)
	print(alex.pay)
	print("--all together-")
	for obj in (bob,sue,alex):
		obj.getRaise(.10)
		print(obj)

	
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	tom = Manager('Tom Jones', 50000)
	development = Department(bob, sue) # Внедрить объекты в составной объект
	development.addMember(tom)
	development.giveRaises(.10)
	# Выполняет giveRaise внедренных объектов
	development.showAll()
