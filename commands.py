import rooms
import dict

#init vals
location = 0
loca = rooms.Cafe()
inventory = ["notepad","boss' note"]

#location translation ig
def locachange():
	global location
	global loca
	if location == 0:
		loca = rooms.Cafe()
	elif location == 1:
		loca = rooms.Playground()
	elif location == 2:
		loca = rooms.Stargazers()
	elif location == 3:
		loca = rooms.Dungeon()
	elif location == 4:
		loca = rooms.Shop()

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
	elif x > rooms.Cafe().unlocked:
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

		else:
			print("That person isn't here.")

	#other rooms
	elif loca.charas != []:
		#playground
		if location == 1:
			print("scrib")
		#stargazers
		elif location == 2:
			print("oli")
		#dungeon
		elif location == 3:
			print("skellie")
		#shop
		elif location == 4:
			print("shopkeep")


	else:
		print("Nobody's here.")


#check [for items]
	#check + display item list but with words
def check():
	print(f"{loca}")
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
	if inventory != ["notepad","boss' note"]:
		pass

	else:
		print("You can't use anything.")
	#check + alter inventory

#save
def save():
	pass

#load
def load():
	pass