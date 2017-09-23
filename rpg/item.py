class Item():

	def __init__(self, item_name, item_description, item_state=""):
		self.name = item_name
		self.description = item_description
		self.state = item_state
		self.responses = {}
		self.container = {}

	def isContainer(self):
		""" Return True if this Item contains other items"""
		return not self.container == {}

	def placeItem(self, item, where):
		"""Place an item inside this item"""
		self.container[where] = item

	def removeItem(self, item_name):
		""" Remove item with name item_name from this item"""
		to_remove = ""
		for it in self.container:
			if self.container[it].getName() == item_name:
				to_remove = it
				break
		if to_remove != "":
			del self.container[to_remove]

	def hasItem(self, item_name):
		""" Return True if this Item contains an Item whose
		getName() function equals item_name
		"""
		for it in self.container:
			if self.container[it].getName() == item_name:
				return True
		return False

	def openUp(self):
		if self.container == {}:
			return False
		self.state = "open"
		return True

	def getDescription(self):
		return self.description

	def getName(self):
		return self.name

	def getState(self):
		""" Get the Item's state. The states Dead and open have meaning
		apart from that, state can be any string
		'"""
		return self.state

	def setState(self, new_state):
		""" Set the Item's state. The states Dead and open have meaning
		apart from that, state can be any string
		'"""

		self.state = new_state

	def addResponse(self, stimuli, response):
		""" addResponse(), canSpeak() and respondTo() are intended to be overridden
		by subclasses of objects cabable of reacting to spoken words
		respondTo(string) is called whenever the user types
		say name string
		The string is a key to a dictionary of methods to be run with the key as parameter.
		"""

		self.responses[stimuli] = response

	def respondTo(self, stimuli):
		""" addResponse(), canSpeak() and respondTo() are intended to be overridden
		by subclasses of objects cabable of reacting to spoken words
		respondTo(string) is called whenever the user types
		say name string
		it should loop through the dictionary maintained by addResponse(), looking
		for a match to stimuli
		if a matching key is found, it should call the value as a function
		
		(See the implementation of this method in Character)
		BUG: There is no deleteResponse()
		"""
		print((self.getName() + " shivers"))

	def canSpeak(self):
		return False

	def fight(self, method):
		print(("Fighting " + self.getName() + "s are we, Don Quijote?"))
		return 0

	def printDetails(self):
		""" Print details about the item and any items it contains"""
		print((self.description + " is " + self.state))
		if self.state == "open":
			for it in self.container:
				print((it + ": " + self.container[it].description))