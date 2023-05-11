#item lookup
def item_desc(x):
	print(gdict.get(f"{x}"))
	print(f"Obtained {x}!")

#displays if an item in a room
cdict = {
	#cafe
	"Cookie":"You also see a cookie on the counter.",
	#playground
	"Shovel":"There's an abandoned plastic shovel in the sandbox.",
	#stargazers
	"Goose":"...is that a goose he's talking to?\nOn second thought, the poor guy actually looks a little distressed at the presence of the goose.",
	#dungeon
	"Moss":"There's some moss in the corner."
	}


#displays when item is grabbed/obtained
gdict = {
	#cafe
	"Cookie":"A delicious treat!",
	#playground
	"Shovel":"A little plastic shovel.",
	"Money":"The child hands you some crumpled up bills.",
	#stargazers
	"Goose":f"You grabbed the goose. It starts honking aggressively, but otherwise does nothing.\nApron guy looks a little awestruck.\n\"Oh, thanks for dealing with that. I didn't know what to do.\"",
	"Soda":"Looks cherry flavored.",
	#dungeon
	"Moss":"Are you going to eat it?",
	"Sword":"The skeleton attempts to escape and drops its sword in the process.",
	"Trinket":"The skeleton drops a trinket.",
	#cafe quest items
	"Pocket Sand":"Good to throw in the eyes of your enemies.",
	"Stickers":"Seems like a child might enjoy these."
	}

chara = {
	"boss":"Your boss is doing.. boss things.",
	"scrib":"There's a child in purple playing in the sandbox.",
	"oli":"You see a guy in a pink apron at the counter.",
	"skel":"There's an armored skeleton. Oh. It's alive.\nYou note that it has a sword, too.",
	"shopkeep":"The shopkeeper looks so tired."
	}

cafechara = {
	"boss":"Your boss is doing.. boss things.",
	"purple child":"You see the kid from the playground eating at one of the tables near a window.",
	"pink barista":"The guy from the other cafe is here too. He's talking to your boss.",
	"skeleton":"The skeleton from the dungeon seems to be drinking... milk?"
	}