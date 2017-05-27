'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.type = 'Animal'
		self.message = ''

	def description(self):
		return '{} the {}'.format(self.name, self.type)

	def speak(self):
		return self.message

	def emote(self):
		print '{} the {} says: {}'.format(self.name, self.type, self.message)

class Dog(Animal):
	def __init__(self, name):
		self.name = name
		self.type = 'Dog'
		self.message = 'Woof!'

class Cat(Animal):
	def __init__(self, name):
		self.name = name
		self.type = 'Cat'
		self.message = 'Meow!'

class Fish(Animal):
	def __init__(self, name):
		self.name = name
		self.type = 'Fish'
		self.message = ''


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
