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

class Manager:
	def __init__(self, name, pay):
		self.person = Person(name, 'mgr', pay)
	
	def getRaise(self, percent, bonus=0.10):
		self.person.getRaise(percent + bonus)

	def __getattr__(self, attr):
		return getattr(self.person, attr)
	def __repr__(self):
		return str(self.person)
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
