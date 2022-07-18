from classtools import AttrDisplay

class Person(AttrDisplay):
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		self.name = self.name.split()[-1]
	def getRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))
class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, 'mgr', pay)
	def getRaise(self, percent, bonus=0.10):
		Person.getRaise(self, percent + bonus)


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
	print(alex)
	alex.getRaise(0.10, 0.10)
	print(alex.pay)
	print("--all together-")
	for obj in (bob,sue,alex):
		obj.getRaise(.10)
		print(obj)
