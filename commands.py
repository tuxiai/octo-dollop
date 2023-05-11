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
					print("...Is this a cafe? Is boss really sending you to a rival business?\nYou're starting to wonder if your boss is sending you on a wild goose chase.")
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
			rooms.cafecharas = ["Boss","Purple Child"]
			rooms.Playground.charas = []
		
		if rooms.Stargazers.quest_status == 2:
			rooms.cafecharas = ["Boss","Purple Child", "Pink Barista"]
			rooms.Stargazers.charas = []

		if rooms.Dungeon.quest_status == 2:
			rooms.cafecharas = ["Boss","Purple Child", "Pink Barista", "Skeleton"]
			rooms.Dungeon.charas = []

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
						inventory.append("Stickers")
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
				print('''You sidestep the goose and walk up to the counter.
“Hello! Welcome to Stargazer Cafe! What can I get for you?”
You show him the paper your boss gave you and ask if they have any.
“Um, sorry. We don’t sell that here. We have plenty of beverages and pastries for you to choose from, though!”
''')
			if loca.quest_status == 2:
				print('''"Enjoy your soda!''')
		#dungeon
		elif location == 3:
			if loca.quest_status == 1:
				print('''"Why hello there, human!"''')
			if loca.quest_status == 2:
				print("The skeleton ran away.")
		#shop
		elif location == 4:
			if loca.quest_status == 1:
				print('''You ask the shopkeeper if they have any of whatever is on this note.
She glances at the note.
"Sorry, we're all out of stock."
man.''')

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
				print("You see a whole host of people here.")
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
		input(f"Obtained {x}!")
		print("\nYour current inventory:")
		inv()

	else:
		print("There's nothing to grab.")


#use
def use():
	global inventory
	global scrib_quest
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
					scrib_quest = 2
					inventory.remove("Stickers")
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

				inventory.remove("Cookie")
				inventory.append("Money")
				loca.quest_status = 2
				rooms.unlocked = 2
			else:
				print("You can't use anything.")

		#stargazers
		elif location == 2:
			if "Money" in inventory:
				print('''After careful consideration, you decide to buy a soda.
“Have a nice day! Give your boss my regards.”
Oh, they know each other. Maybe it’s not a rivalry, after all.''')
				dict.item_desc("Soda")

				inventory.remove("Money")
				inventory.append("Soda")
				loca.quest_status = 2
				rooms.unlocked = 3
			else:
				print("You can't use anything.")

		#dungeon
		elif location == 3:
			sand = False
			if "Pocket Sand" in inventory:
				sand = True
				print("You throw the sand at the skeleton's eye sockets.\nIt covers its sockets as if in pain.")
				inventory.remove("Pocket Sand")
			elif "Goose" in inventory:
				print("You unleash the goose.\nThe skeleton shrieks in terror.")
				if sand:
					print("Its terror seems amplified because of its impaired vision.")
					dict.item_desc("Trinket")
					inventory.append("Trinket")
				print("The goose honks.")
				dict.item_desc("Sword")

				inventory.remove("Goose")
				inventory.append("Sword")
				loca.quest_status = 2
				rooms.unlocked = 4
			else:
				print("You can't use anything.")

		#shop
		elif location == 4:
			if ["Shovel","Soda","Sword","Moss"] not in inventory:
				print("No one seems to want anything you have.\nMaybe see if you can find anything else from the other doors.")
			elif "Shovel" in inventory:
				print("You trade the plastic shovel you found for a toy truck.")
				inventory.remove("Shovel")
				inventory.append("Truck")
			elif "Soda" in inventory:
				if "Truck" in inventory:
					print("You trade the cherry soda and toy truck for a strange mirror.")
					inventory.remove("Soda")
					inventory.remove("Truck")
					inventory.append("Mirror")
				elif "Truck" not in inventory:
					print('''"Hey, that soda looks pretty good!"
"I have a magic mirror, but I don't really feel like it's worth only a soda."
"If you can find something to sweeten the deal, I'll definitely trade with you!"''')
			elif "Sword" in inventory:
				if "Mirror" in inventory:
					print('''"Whoa! That sword and mirror look super cool!"
"Here, I'll trade you."
You trade the sword and weird mirror for a.. mushroom? Alright then.''')
					inventory.remove("Sword")
					inventory.remove("Mirror")
					inventory.append("Mushroom")
			elif "Moss" in inventory:
				if "Mushroom" in inventory:
					print('''A teenager approaches you.
"Hey, that moss and mushroom look pretty neat. I'll trade you this [] for it"
You trade with the teenager.''')
					inventory.remove("Moss")
					inventory.remove("Mushroom")
					inventory.append("Duck")

	else:
		print("You can't use anything.")

#save
def save():
	pass

#load
def load():
	pass