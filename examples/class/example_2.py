# -*- coding: utf-8 -*-

# refer to https://www.learncodewithmike.com/2020/01/python-inheritance.html

# ==================================
# Multi-Level Inheritance

class Transportation():
	def __init__(self):
		self.color = "white"

class Transportation_air(Transportation):
	def accelerate(self):
		print("accelerate method is called")

class Airplane(Transportation_air):
	def control(self):
		print("control method is called")

myLittlePlane = Airplane()
print(myLittlePlane.color)
myLittlePlane.accelerate()
myLittlePlane.control()

# ==================================
# Multiple Inheritance

class Transportation():
	def __init__(self):
		self.color = "white"

	def drive(self):
		print("drive method is called")

class Transportation_control():
	def __init__(self):
		pass
	def openAC(self):
		print("openAC method is called")

class Car(Transportation, Transportation_control):
	pass

mazda = Car()
mazda.drive()
mazda.openAC()
