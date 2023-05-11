import rooms
import dict

#init vals
location = 0
loca = rooms.Cafe
inventory = ["Notepad","Boss' Note"]

#scrib quest lol
scrib_quest = 0

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
	try:
		x = int(input("Which door number?\n"))
		if x not in range(0,5):
			print("That door doesn't exist.")
		elif x > rooms.unlocked:
			print("That door is locked.")
		else:
			location = x
			print("You enter the door.")
			locachange()

			if loca.quest_status == 0:
				if location == 1:
				#playground
					print("You're at... a playground? Would the boss' thing really be here?")
					rooms.Playground.quest_status = 1
				if location == 2:
				#stargazers
					print("...Is this a cafe? Is boss really sending you to a rival business?\nYou're staring to wonder if your boss is sending you on a wild goose chase.")
					rooms.Stargazers.quest_status = 1
				if location == 3:
				#dungeon
					print("A dungeon???? You're seriously questioning boss' sanity here.\nDo they even know where these doors lead?")
					rooms.Dungeon.quest_status = 1
				if location == 4:
				#shop
					print("A shop! Maybe you can find what your boss needs here.")
					rooms.Shop.quest_status = 1
			else:
				print(loca)
	except ValueError:
		print("That's not a number.")

	#leave
def leave():
	global location
	if location == 0:
		print("You're still on shift. You can't leave.")
	else:
		#change character location
		if rooms.Playground.quest_status == 2:
			rooms.cafecharas.append("Purple Child")
			rooms.Playground.charas.remove(rooms.Playground.charas[0])

		#change player location
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
		for i in rooms.cafecharas:
			print(f"-{i}")
		x = input()
		if x.title() in rooms.cafecharas:
			if x.lower() == "boss":
				print('''"Hiya. Haven't found it yet?"
"Chin up. You'll find it by the end of the day. Probably."''')

			#trade stickers for pocket sand from scrib
			global scrib_quest
			if x.lower() == "purple child":
				if scrib_quest == 0:
					print('''"Oh hey, it's you! Hey, I have a favor to ask. Can you find me some stickers?"
The kid continues before you have the chance to decline.
"Cool, thanks!"''')
					scrib_quest = 1
				elif scrib_quest == 1:
					print('''"Have you gotten the stickers yet? No? Okay!"''')
				elif scrib_quest == 2:
					print('''"Hi!!"''')

			#get stickers from oli
			if x.lower() == "pink barista":
				print('''He pauses in his conversation with your boss.
"Oh, hello again. Did you need something?"''')
				if scrib_quest == 1:
					if "Stickers" not in inventory:
						print(f'''"Stickers? Yeah, I have some. Here."
	He reaches into his pocket and pulls out a sticker sheet.''')
						dict.item_desc("Stickers")
				else:
					print('''"Nothing? Ah, okay."
He continues conversing with your boss.''')

			if x.lower() == "skeleton":
				print("It's ignoring you.")

		else:
			print("That person isn't here.")

	#other rooms
	elif loca.charas != []:
		#playground
		if location == 1:
			if loca.quest_status == 1:
				print('''You ask if the child can read the note from your boss.
The child seems to pay you no mind, only mumbling to themself.
"Man, I'm kinda hungry... But this sandcastle won't build itself! I have to stick with it!!"''')
			if loca.quest_status == 2:
				if loca.charas != []:
					print("You try to ask the child about the note, but they're too focused on their sandcastle to respond.")
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

	#charas
	if location == 0:
		for i in rooms.cafecharas:
			print(dict.cafechara.get(f"{i.lower()}"))

	elif location != 0:
		for i in loca.charas:
			print(dict.chara.get(f"{i.lower()}"))
		#other
		#playground
		if location == 1:
			if rooms.Playground.charas != []:
				print("The playground seems pretty deserted, save for that kid.")
		#stargazers

		#dungeon
		elif location == 3:
			if rooms.Dungeon.charas != []:
				print("Skeleton aside, there's a lot of things in here: moss, gold, even a treasure chest.")
			else:
				print("There's a lot of things in here: moss, gold, even a treasure chest.")
		#shop
		elif location == 4:
			x = False
			if not x:
				print("You see a whole host of people here. The shopkeep behind the counter looks very tired.")
				x = True
			if x:
				print("After looking more closely at the people, you notice that there seems to be some sort of trading circle going on.")

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
	global inventory
	#check + alter inventory
	if inventory != ["Notepad","Boss' Note"]:
		#cafe
		if location == 0:
			if scrib_quest == 1:
				if "Stickers" in inventory:
					print('''You gave the stickers to the child.
"Thanks! Here's some sand. You can throw it at people or something."
The kid gives you a handful of sand.
Obtained Pocket Sand.''')
					inventory.append("Pocket Sand")

		#playground
		if location == 1:
			if "Cookie" in inventory:
				input('''You gave the child a cookie. They look at you in wonder.
"Whoa, thanks!"
"Wait, I didn't pay for this..."''')
				print('''The child starts patting their pockets.
"Aha! Here's some money for the cookie!''')
				dict.item_desc("Money")
				print("The child immediately goes back to making their sandcastle.")

				loca.quest_status = 2
				rooms.unlocked = 2
			else:
				print("You can't use anything.")

		#stargazers
		elif location == 2:
			if "Money" in inventory:
				pass
			else:
				print("You can't use anything.")

	else:
		print("You can't use anything.")

#save
def save():
	pass

#load
def load():
	pass