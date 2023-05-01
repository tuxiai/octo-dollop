import commands
import rooms

#init variables
location = "a"
inventory = []
inp = ''
goal = False

#Beginning
while inp not in ["talk","t"]:
	inp = input("Another day, another shift. You should [talk] to your boss.\n")
	if inp in ["talk", "t"]:
		print('''Your boss smiles at you.
"Morning. I need you to get this for me. Thanks."
They hand you a note that you can't read.
"You can probably find it through one of these doors."''')
		break

#game start!
while inp not in ["c", "check"]:
	inp = input("Don't forget to [check] for anything you might need.\n")

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