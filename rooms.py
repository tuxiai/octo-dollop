#basic room template
class room():
	#item + character list
	def __init__(self):
		self.items = []
		self.charas = []
		#for determining what dialogue to show
		#0: init
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
		self.quest_status = 0

	#description
	def __str__(self):
		#the actual desc
		a = "A cute little playground."

		#init
		if self.quest_status == 0:
			x = f"You're at... a playground? Would the boss' thing really be here?"
			self.quest_status = 1
		#scrib left
		elif self.charas == []:
			x = f"{a}\nNo one's here."
		#all stages
		elif self.quest_status in range(3):
			x = f"{a}\nIt seems pretty deserted, save for that kid."

		return f"{x}"

#Door 2
class Stargazers():
	#item + character list
	def __init__(self):
		self.items = ["goose"]
		self.charas = ["oli"]
		self.quest_status = 0

	#description
	def __str__(self):
		if self.quest_status == 0:
			x = f"...Is this a cafe? Is boss really sending you to a rival business??\nYou're starting to wonder if your boss is sending you on a wild goose chase."
			self.quest_status = 1

		if self.quest_status in range(3):
			x = f"A nice little cafe. It's pretty sunny."

		if "goose" in self.items:
			x = x + f"\n...Is that a goose talking to the barista?\nOn second thought, the poor guy actually looks a little distressed at the presence of the goose."

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