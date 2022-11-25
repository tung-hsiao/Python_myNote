# -*- coding: utf-8 -*-

# refer to https://www.learncodewithmike.com/2020/01/python-inheritance.html

# ==================================
# Base class
class Transportation():
	def __init__(self):
		self.color = "white"

	def drive(self):
		print("drive method is called")

# Sub class
class Car_1(Transportation):
	def accelerate(self):
		print("accelerate method is called")

# Sub class
class Airplane(Transportation):
	def fly(self):
		print("fly method is called")


mazda = Car_1()
mazda.drive()
print(mazda.color)
print("")

# ==================================
print(issubclass(Airplane, Transportation))  # True
print(issubclass(Airplane, Car_1))             # Fasle
print("")


# ==================================
class Car_2(Transportation):
	def drive(self):
		print("Sub class drive method is called")
mazda = Car_2()
mazda.drive()
print("")


# ==================================
class Car_3(Transportation):
	def drive(self):
		super().drive()
		print("Sub class drive method is called")
mazda = Car_3()
mazda.drive()
