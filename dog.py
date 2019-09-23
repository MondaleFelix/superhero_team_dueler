#  dog.py

class Dog:

	#  constructer that runs whenever a new instance of your class is created
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

	def bark(self):
		print( self.name + " woofs")

	def sit(self):
		print(self.name + " sits")

	def roll(self):
		print(self.name + " rolls over")

