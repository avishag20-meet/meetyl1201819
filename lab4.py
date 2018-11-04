#class animal (object):
	#def __init__(self,sound,name,age,favorite_color):
#		self.sound = sound
#		self.name = name
#		self.age = age
#		self.favorite_color = favorite_color
#	def eat (self,food):
#		print ("Yummy!! " +self.name + "is eating a " +food)
#	def description(self):
#		print (self.name + "is " + self.age + "years old and loves the color " +self.favorite_color)
#	def make_sound (self):
#		print ("oink!! "*3)	

#pig = animal ("oink", "Robert ", "22 ", "red")
#pig.eat("banana!")
#pig.description ()
#pig.make_sound ()

class person (object):
	def __init__(self, name, sound, age, city, gender, food):
		self.name = name
		self.sound = sound
		self.age = age
		self.city = city
		self.gender = gender
		self.food = food
	def eat (self):
		print (self.name + " is eating " +self.food)
	def birthday (self):
		print (self.name + " is " + self.age + " years old")

man = person ("Dolores", "wow", "68", "london", "male", "knedalach")
man.eat()
man.birthday()

