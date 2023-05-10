#*sigh*
cafecharas = ["boss"]
unlocked = 1

#Cafe 0
class Cafe():
	#item + character list
	def __init__(self):
		self.items = ["cookie"]
		self.charas = ["boss"]

	#description
	def __str__(self):
		if unlocked == 1:
			x = "You see four doors. 1 seems to be unlocked."
		elif unlocked in range (1,5):
			x = f"You see four doors. {unlocked} seem to be unlocked."
		return f"The cafe you work at. It's cozy here.\n{x}"
		
#basic room template
class room():
	#item + character list
	def __init__(self,items = [],charas = [],desc):
		self.items = items
		self.charas = charas
		self.desc = desc
		#for determining what dialogue to show
		#0: init
		#1: in progress
		#2: finished
		self.quest_status = 0

	#description
	def __str__(self):
		return self.desc

#door 1
Playground = room(["pocket sand"],["scrib"],"A cute little playground.")

#door 2
Stargazers = room(["goose"],["oli"],"A nice little cafe. It's pretty sunny.")

#door 3
Dungeon = room()

#door 4
Shop = room()