#*sigh*
cafecharas = ["boss"]
unlocked = 1
		
#basic room
class room():
	#item + character list
	def __init__(self,items = [],charas = [],desc = ""):
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

#cafe 0
Cafe = room(["cookie"],["boss"],"The cafe you work at. It's cozy here.")

#door 1
Playground = room(["pocket sand"],["scrib"],"A cute little playground.")

#door 2
Stargazers = room(["goose"],["oli"],"A nice little cafe. It's pretty sunny.")

#door 3
Dungeon = room()

#door 4
Shop = room()