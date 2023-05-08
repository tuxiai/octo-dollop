import rooms
import commands
import dict

####################
#init variables
inp = ''
goal = False
#!!REMOVE 'x' IN FINAL!!
cmds = ["x","quit","q","help","h","inventory","i","talk","t","check","c","grab","g","use","u","save","s","load","l","door","leave"]

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
		commands.cmdlist()
		inp = input("You also see a cookie on the counter.\n")
		break

####################
#command loop
while inp not in ['q','quit'] and not goal:
	while inp not in cmds:
		inp = input()

	#controls
	#"h" or "help" for a list of commands
	if inp in ["help","h"]:
		commands.cmdlist()
		inp = ''
	#"i" or "inventory" to see your items
	elif inp in ["inventory","i"]:
		commands.inv()
		inp = ''
	#"t" or "talk" to talk to characters
	elif inp in ["talk","t"]:
		commands.talk()
		inp = ''
	#"c" or "check" to check a room for items
	elif inp in ["check","c"]:
		commands.check()
		inp = ''
	#"g" or "grab" to take an item
	elif inp in ["grab","g"]:
		commands.grab()
		inp = ''
	#"u" or "use" to use an item
	elif inp in ["use","u"]:
		commands.use()
		inp = ''
	#"s" or "save" to save
	elif inp in ["save","s"]:
		commands.save()
		inp = ''
	#"l" or "load" to load
	elif inp in ["load","l"]:
		commands.load()
		inp = ''
	#"door" to enter that room
	elif inp in ["door"]:
		commands.door()
		inp = ''
	#"leave" to leave the room you're in
	elif inp in ["leave"]:
		commands.leave()
		inp = ''
#!!FOR TESTING!!
	elif inp == 'x':
		goal = True

####################
#game start!

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