#basic room template
class room():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []

	#description
	def __str__(self):
		return ""

#Cafe 0
class Cafe():
	def __init__(self):
		self.items = ["cookie"]
		self.charas = ["boss"]
		self.unlocked = 1

	def __str__(self):
		if self.unlocked == 1:
			x = "You see four doors. 1 seems to be unlocked."
		else:
			x = f"You see four doors. {self.unlocked} seem to be unlocked."
		return f"The cafe you work at. It's cozy here.\n{x}"

#Door 1

#Door 2

#Door 3

#Door 4
