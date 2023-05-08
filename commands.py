import rooms

#location
location = 0

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
	print(inventory)

#talk
def talk():
	pass
	#check character list + progress

#check [for items]
	#check + display item list but with words
def check():
	if location == 0:
		print(f"{rooms.Cafe()}\n")

#grab
def grab():
	pass
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