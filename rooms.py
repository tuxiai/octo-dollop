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

		#init
		if self.quest_status == -1:
			x = f"You're at... a playground? Would the boss' thing really be here?"
			self.quest_status = 0
		#scrib left
		elif self.charas == []:
			x = f"{a}\nNo one's here."
		#all stages
		elif self.quest_status in range(-1,3):
			x = f"{a}\nIt seems pretty deserted, save for that kid."

		return f"{x}"

#Door 2
class Stargazers():
	#item + character list
	def __init__(self):
		self.items = ["goose"]
		self.charas = ["oli"]
		self.quest_status = -1

	#description
	def __str__(self):
		a = "A nice little cafe. It's pretty sunny."
		b = "You're starting to wonder if you boss is sending you on a wild goose chase."

		if self.quest_status == -1:
			x = f"...Is this a cafe? Is boss really sending you to a rival business??\n{b}"


		return f"{x}"

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