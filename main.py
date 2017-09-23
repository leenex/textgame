# -*- coding: utf-8 -*-
import os
import rpg

life_words = ["unrecognizably smashed",
"gutted",
"barely alive",
"shitkicked",
"busted up",
"thrashed",
"beaten",
"still okay",
"feeling fine",
"the man",
"on pervitin"]
life = 8

items = {}


def inventory():
	print("\n---- You have ---")
	for i in items:
		print(items[i].getName())
	print("\n---------\n")


def check_inventory(item_to_find):
	for i in items:
		if items[i].getName() == item_to_find:
			return items[i]
	return {}

kitchen = rpg.Room("Kitchen")
dining_hall = rpg.Room("Dining hall")
ballroom = rpg.Room("Ballroom")

kitchen.setDescription("A dank and dirty room buzzing with flies. There is a stench of rotten meat.")
dining_hall.setDescription("A large room with ornate golden decorations on every wall.")
ballroom.setDescription("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance")

kitchen.linkRoom(dining_hall, "south")
dining_hall.linkRoom(kitchen, "north")
dining_hall.linkRoom(ballroom, "west")
ballroom.linkRoom(dining_hall, "east")

currentRoom = kitchen


def find_item(item_name):
	for it in currentRoom.items:
		item = currentRoom.items[it]
		if item.getName() == item_name:
			return currentRoom.items[it]
		if item.getState() == "open":
			for cit in item.container:
				if item.container[cit].getName() == item_name:
					return item.container[cit]
	return {}


def take_item(item_name):
	item = find_item(item_name)
	if item == {}:
		print(("I see no " + item_name + " here!"))
	else:
		items[item_name] = item
		currentRoom.removeItem(item_name)


def describe_item(item_name):
	item = find_item(item_name)
	if item == {}:
		print(("I see no " + item_name + " here!"))
	else:
		print((item.getDescription()))


def openItem(item_name):
	item = find_item(item_name)
	if item == {}:
		print(("There is no " + item_name + " here!"))
	else:
		if item.openUp():
			print((item.getName() + " springs open"))
		else:
			print((item.getName() + " won't open, even whem using a sledgehammer"))


def fight_enemy(enemy, method):
	cost = 0
	weapon = check_inventory(method)
	if weapon == {} and method != "joke":
		print(("Don't bullshit a bullshitter, Mylord. What " + method + " would that be? Checked your inventory lately?"))
		print("take, grab, snatch is what I say")
		return 0
	print ("Fight!")
	who = find_item(enemy)
	if who == {}:
		print(("No " + enemy + " in sight"))
		return 0
	print(("Lunging " + method + " at " + who.getName()))
	cost = who.fight(method)
	return cost


def holler():
	print("\n>>Hello (hello, hello, ...), is there anybody in there?")
	print(">>Is there any one at home?")
	for it in currentRoom.items:
		item = currentRoom.items[it]
		if item.canSpeak():
			item.respondTo("hello")
	print("\n(Pst! If you want to speak to someone in particular, use:")
	print("say name word)\n")


def speak(words):
	if len(words) < 2:
		who = input(("With whom did you wish to converse, Sire?"))
	else:
		who = words[1]
	interlocutor = find_item(who)
	if interlocutor == {}:
		print((who + " is not here."))
		return
	if len(words) < 3:
		what = input("And what message did you wish to convey to this " + interlocutor.getDescription() + "?")
	else:
		what = words[2]
	interlocutor.respondTo(what)

revolver = rpg.Item("revolver", "A shiny, metal object", "loaded")
dishWasher = rpg.Item("dishwasher", "A large kitchen appliance", "closed")
pill = rpg.Item("pill", "Something that cures headaches, perhaps even gonorrhea and cancer", "glowing")
dishWasher.placeItem(pill, "inside")
towel = rpg.Item("towel", "Something fluffy, full of magic dust and cobwebs", "dry and ready")

troll = rpg.Character("Busey", "A big, hairy troll", "angry")
troll.addResponse("up", lambda x: troll.speak("I wish I could, but I'm too fat, mate"))

alex = rpg.Enemy("Alex", "A very, very bad radio host", "baleful")
alex.addResponse("silence", lambda x: alex.speak("OOOPS!!\n *Unfortunately, Alex uses epithets unsuitable for print*"))
alex.addFightResponse("revolver", lambda x: alex.killWith("guhn"))


def daveHelpPill(word):
	if word == "dishwasher":
		dave.speak(word + "? Let me take a look. Yes, there's a pill in here")
	if word == "headache":
		dave.speak("Too much of that Cuban rum, huh? Why don't you take a pill?")
	dave.setState("compassionately")
	dave.speak("Pills cure all kinds of ailments, except, perhaps, broken bones")


def daveHelpTowel(word):
	dave.speak("Hmm ... " + word + ", you say? I wonder if it could be a towel")

dave = rpg.Friend("Dave", "A retired school teacher")
dave.addResponse("help", lambda x: dave.speak("Sure, my friend, I can give you a hint"))
dave.addResponse("hint", lambda x: dave.speak("Be specific. You know that towels are fluffy, right?"))
dave.addResponse("haggis", lambda x: dave.speak("Someone has to feed the trolls"))
dave.addResponse("yuck", lambda x: dave.speak("If you think this stinks, wait until you smell Alex' breath"))
dave.addResponse("headache", daveHelpPill)
dave.addResponse("gonorrhea", daveHelpPill)
dave.addResponse("cancer", daveHelpPill)
dave.addResponse("glowing", daveHelpPill)
dave.addResponse("dishwasher", daveHelpPill)
dave.addResponse("fluffy", daveHelpTowel)
dave.addResponse("cobweb", daveHelpTowel)
dave.addResponse("chandelier", daveHelpTowel)

kitchen.placeItem(dishWasher, "in the corner")
kitchen.placeItem(dave, "stirring a pot full of foul-smelling haggis")
dining_hall.placeItem(towel, "dangling from a chandelier")
dining_hall.placeItem(troll, "seated at the table")
dining_hall.placeItem(revolver, "in the troll's hand")
ballroom.placeItem(alex, "in front of a microphone")

while life > 0:
	if life > 10:
		life = 10
	currentRoom.printDetails()
	command = input("You're " + life_words[life] + '. What next? >')
	if command == "end":
		break
	print(">\n<")
	arg = command.split(" ")
	arg[0].lower()
	if arg[0] in ["north", "south", "east", "west"]:
		currentRoom = currentRoom.move(command)
	elif arg[0] == "inventory":
		inventory()
	elif arg[0] in ["describe", "show"]:
		if len(arg) < 2:
			print("describe what, my Lord?")
		else:
			describe_item(arg[1])
	elif arg[0] in ["talk", "speak", "say", "um,"]:
		speak(arg)
	elif arg[0] in ["hello", "yell", "holler", "whistle"]:
		if len(arg) < 2:
			holler()
		else:
			speak(arg)
	elif arg[0] in ["take", "grab", "snatch", "steal", "acquire", "commandeer"]:
		if len(arg) < 2:
			what = input("Take what, Mylord?")
			take_item(what)
		else:
			take_item(arg[1])
	elif arg[0] in ["fight", "kill", "murder", "whack", "keelhaul", "strangle"]:
		if len(arg) < 2:
			who = input("With whom did you wish to do battle, Sire?")
		else:
			who = arg[1]
		if len(arg) < 3:
			what = input("What weapon will you be using in this risky endeavor, Mylord?")
		else:
			what = arg[2]
		life = life - fight_enemy(who, what)
	elif arg[0] in ["open", "kick" ]:
		openItem(arg[1])
	else:
		print(("Never " + arg[0] + " in a " + currentRoom.getName() + "!"))
	print("<")
print("We are gathered here today to remember " + os.getenv("LOGNAME"))
print("Such a legendary hero will be sorely missed.")