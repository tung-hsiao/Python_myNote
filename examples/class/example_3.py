
# refer to https://dboyliao.medium.com/python-%E7%B9%BC%E6%89%BF-543-bc3d8ef51d6d

class Equus:
    def __init__(self, is_male):
        pass
    def run(self):
        print("I run at speesd {}".format(self.speed))
        print('I\'m {}'.format(self.gender))
    def roar(self):                    # add
    	print("Equus Equus Equus")

class Horse(Equus):
    def __init__(self, is_male):
        print('Horse init')
        self.speed = 30
        self.gender = 'male' if is_male else 'female'
        self.is_horse = True
    def roar(self):
        print('Horse Horse Horse')
        super().roar()                   # add

class Donkey(Equus):
    def __init__(self, is_female):
        print('Donkey init')
        self.speed = 20
        self.gender = 'female' if is_female else 'male'
        self.is_donkey = True
    
    def roar(self):
        print('Donkey Donkey Donkey')
        super().roar()                   # add

class Mule(Horse, Donkey):
	def __init__(self, is_male):
		print("Mule init")
		super().__init__(is_male)
	def roar(self):
		print("Mule Mule Mule")
		super().roar()

M = Mule(is_male=True)
# Mule init
# Horse init               -> Think !!! why this happens?

M.roar()
# Mule Mule Mule
# Horse Horse Horse
# Donkey Donkey Donk       -> Think !!! why this happens?
# Equus Equus Equus

class Mule2(Donkey, Horse):
    def __init__(self, is_male):
        print('Mule init')
        super().__init__(is_male)
    
    def roar(self):
        print('Mule Mule Mule')
        super().roar()

M = Mule2(is_male=True)
# Mule init
# Donkey init            -> class order will change the result
M.roar()
# Mule Mule Mule
# Donkey Donkey Donkey
# Horse Horse Horse
# Equus Equus Equus
