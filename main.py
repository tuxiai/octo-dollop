import rooms

####################
#init variables
location = '0'
inventory = []
inp = ''
goal = False
cmds = ['h','help','i','inventory','t','talk','c','check','g','grab','u','use','s','save','l','load','door','leave']

####################
#commands
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
	if x not in range(1,5):
		print("That door doesn't exist.")
	else:
		location = x

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

####################
#Beginning
while inp not in ["talk","t"]:
	inp = input("Another day, another shift. You should [talk] to your boss.\n")
	if inp in ["talk", "t"]:
		print('''Your boss smiles at you.
"Morning. I need you to get this for me. Thanks."
They hand you a note that you can't read.
"You can probably find it through one of these doors."''')
		break
while inp not in ["c", "check"]:
	inp = input("Don't forget to [check] for anything you might need.\n")
	if inp in ["c", "check"]:
		print(f'''The cafe you work at. It's cozy here.
You find a strange paper. It reads:''')
		cmdlist()
		inp = input("You also see a cookie on the counter.\n")
		break

####################
#game start!
####################
#command loop
while not goal:
	#controls
	#"h" or "help" for a list of commands
	if inp in ["help","h"]:
		cmdlist()
	#"i" or "inventory" to see your items
	elif inp in ["inventory","i"]:
			inv()
	#"t" or "talk" to talk to characters
	elif inp in ["talk","t"]:
		talk()
	#"c" or "check" to check a room for items
	elif inp in ["check","c"]:
		check()
	#"g" or "grab" to take an item
	elif inp in ["grab","g"]:
		grab()
	#"u" or "use" to use an item
	elif inp in ["use","u"]:
		use()
	#"s" or "save" to save
	elif inp in ["save","s"]:
		save()
	#"l" or "load" to load
	elif inp in ["load","l"]:
		load()
	#"door" to enter that room
	elif inp in ["door","d"]:
			door()
	#"leave" to leave the room you're in
	elif inp in ["leave","l"]:
		leave()

####################


####################
#End
if goal:
	input('''"Success! You've obtained []!"
After the shock of a literal popup appearing subsides, you look at the object in your hands.
It's... a rubber duck. Seriously?
This is what your boss wanted"
Ah, whatever. You should get this to your boss.
''')
	input('''Your boss looks at you when they notice the duck in your hands.
"Hey, nice job. I knew you could find it."
They pat you on the back.
"Go ahead and leave for the day. I can take care of the cafe."
''')
	print('''"Oh, and take a snack for the road." They slide a plate of cookies in your direction.
You take a snack and clock out.
Nice job! Now go get a snack in real life--and maybe drink some water too.''')