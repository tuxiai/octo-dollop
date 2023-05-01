#help
def cmds():
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

Movement:
"door [number]" to enter that door
"leave" to leave the room you're in
	(leaving a room will take you back to the cafe)

P.S. Press enter to advance text!
=====
''')

#movement
	#door x
	#leave
def leave():
	if location == 'a':
		print("You're still on shift. You can't leave.")
	else:
		location = 'a'
		print("You're back in the cafe.")

#inventory
def inv():
	print(inventory)

#talk
#check [for items]
#grab
#use
#save
#load