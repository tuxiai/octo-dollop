import rooms
import dict

#init vals
location = 0
inventory = ["notepad","boss' note"]

#location translation ig
if location == 0:
	loca = Cafe()
elif location == 1:
	loca = 

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
	x = input("Which door number?\n")
	if x not in range(0,5):
		print("That door doesn't exist.")
	else:
		location = x
		print("You enter the door.")

	#leave
def leave():
	if location == 0:
		print("You're still on shift. You can't leave.")
	else:
		location = 0
		print("You're back in the cafe.")

#inventory
def inv():
	for i in inventory:
		print(i)

#talk
def talk():
	#check character list + progress
	#only cafe has multiple characters
	if location == 0:
		print("To who?")
		for i in rooms.Cafe().charas:
			print(f"-{i}")
		inp = input()
		if inp in rooms.Cafe().charas:
			print("cool")
		else:
			print("That person isn't here.")
	if location in range(0,4):
		pass
	else:
		print("Nobody's here.")


#check [for items]
	#check + display item list but with words
def check():
	if location == 0:
		print(f"{rooms.Cafe()}")
		for i in rooms.Cafe().items:
			print(dict.cdict.get(f"{i}"))

#grab
def grab():
	#check + alter item list
	

#use
def use():
	pass
	#check + alter inventory

#save
def save():
	pass

#load
def load():
	pass