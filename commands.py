import rooms
import dict

#init vals
location = 0
loca = rooms.Cafe
inventory = ["notepad","boss' note"]

#location translation ig
def locachange():
	global location
	global loca
	if location == 0:
		loca = rooms.Cafe
	elif location == 1:
		loca = rooms.Playground
	elif location == 2:
		loca = rooms.Stargazers
	elif location == 3:
		loca = rooms.Dungeon
	elif location == 4:
		loca = rooms.Shop

#help
def cmdlist():
	print('''=====
Commands:
"h" or "help" for a list of commands
"i" or "inventory" to see your items
"t" or "talk" to talk to characters
"c" or "check" to check a room for items
"g" or "grab" to take an item
"u" or "use" to use an item
"s" or "save" to save
"l" or "load" to load
"q" or "quit" to quit

Movement:
"door" to enter that room
"leave" to leave the room you're in
	(leaving a room will take you back to the cafe)

P.S. Press enter to advance text!
=====
''')

#movement
	#door x
def door():
	global location
	x = int(input("Which door number?\n"))
	if x not in range(0,5):
		print("That door doesn't exist.")
	elif x > rooms.unlocked:
		print("That door is locked.")
	else:
		location = x
		print("You enter the door.")
		locachange()
		print(loca)

	#leave
def leave():
	global location
	if location == 0:
		print("You're still on shift. You can't leave.")
	else:
		print("You're back in the cafe.")
		location = 0
		locachange()

#inventory
def inv():
	for i in inventory:
		print(f"- {i}")

#talk
def talk():
	#check character list + progress
	#only cafe has multiple characters
	if location == 0:
		print("To who?")
		for i in loca.charas:
			print(f"-{i}")
		x = input()
		if x in loca.charas:
			if x.lower() == "boss":
				print("Hiya. Haven't found it yet?")
				print("Chin up. You'll find it by the end of the day. Probably.")
			#get trade stickers for pocket sand from scrib
			if x.lower() == "purple child"
			#get stickers from oli

		else:
			print("That person isn't here.")

	#other rooms
	elif loca.charas != []:
		#playground
		if location == 1:
			if loca.quest_status == 1:
				pass
			if loca.quest_status == 2:
				pass
		#stargazers
		elif location == 2:
			if loca.quest_status == 1:
				pass
			if loca.quest_status == 2:
				pass
		#dungeon
		elif location == 3:
			if loca.quest_status == 1:
				pass
			if loca.quest_status == 2:
				pass
		#shop
		elif location == 4:
			if loca.quest_status == 1:
				pass
			if loca.quest_status == 2:
				pass


	else:
		print("Nobody's here.")


#check [for items]
	#check + display item list but with words
def check():
	global location
	print(f"{loca}")

	#characters
	if location == 0:
		for i in rooms.cafecharas:
			print(dict.cafechara.get(f"{i}"))

	elif location != 0:
		for i in loca.charas:
			print(dict.chara.get(f"{i}"))

	#items
	for i in loca.items:
		print(dict.cdict.get(f"{i}"))

#grab
def grab():
	#check + alter item list
	if loca.items != []:
		#grab the item
		x = loca.items[0]
		#add to inv
		inventory.append(x)
		#remove from room
		loca.items.remove(x)

		print(dict.gdict.get(f"{x}"))
		print(f"Obtained {x}!")
		print("Your current inventory:")
		inv()

	else:
		print("There's nothing to grab.")


#use
def use():
	#check + alter inventory
	if inventory != ["notepad","boss' note"]:
		#playground
		if location == 1:
			if "cookie" in inventory:
				pass
		#stargazers
		elif location == 2:
			if "money" in inventory:
				pass


	else:
		print("You can't use anything.")

#save
def save():
	pass

#load
def load():
	pass