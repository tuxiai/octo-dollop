#basic room template
class room():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []
		#for determining what dialogue to show
		#0: not started
		#1: in progress
		#2: finished
		self.quest_status = 0

	#description
	def __str__(self):
		return ""

	#check str
	def check(self):
		return

#Cafe 0
class Cafe():
	#item + character list
	def __init__(self):
		self.items = ["cookie"]
		self.charas = ["boss"]
		self.unlocked = 1

	#description
	def __str__(self):
		if self.unlocked == 1:
			x = "You see four doors. 1 seems to be unlocked."
		else:
			x = f"You see four doors. {self.unlocked} seem to be unlocked."
		return f"The cafe you work at. It's cozy here.\n{x}"

#Door 1
class Playground():
	#item + character list
	def __init__(self):
		self.items = ["pocket sand"]
		self.charas = ["scrib"]
		self.quest_status = -1

	#description
	def __str__(self):
		#the actual desc
		a = "A cute little playground."
		#bc I don't want to retype that lol
		y = "You see a child in purple playing in the sandbox."

		#init
		if self.quest_status == -1:
			x = f"You're at... a playground? Would the boss' thing really be here?\n{y}"
			self.quest_status = 0
		#scrib left
		elif self.charas == []:
			x = f"{a}\nNo one's here."
		#all stages
		elif self.quest_status in range(-1,3):
			x = f"{a}\n{y}\nIt seems pretty deserted, save for that kid."

		return f"{x}"

#Door 2
class Stargazers():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []
		self.quest_status = 0

	#description
	def __str__(self):
		return ""

#Door 3
class Dungeon():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []
		self.quest_status = 0

	#description
	def __str__(self):
		return ""

#Door 4
class Shop():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []
		self.quest_status = 0

	#description
	def __str__(self):
		return ""