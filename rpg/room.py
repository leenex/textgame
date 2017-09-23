class Room():

	def __init__(self, room_name):

		self.name = room_name
		self.description = None
		self.linkedRooms = {}
		self.items = {}

	def setDescription(self, room_description):
		self.description = room_description

	def getDescription(self):
		return self.description

	def setName(self, new_name):
		self.name = new_name

	def getName(self):
		return self.name

	def linkRoom(self, roomToLink, direction):
		self.linkedRooms[direction] = roomToLink

	def placeItem(self, item_to_place, where_in_the_room):
		""" Place an Item in the room
		Example:
			room = Room("kitchen")
			diswasher = Item("dishwasher", "A large kichen appliance", "closed")
			kitchen.placeItem(dishwasher, "In the corner")
		"""
		self.items[where_in_the_room] = item_to_place

	def removeItem(self, item_name):
		""" Remove the item whose getName() function equals item_name
		If the item is contained within another item, it will be removed as well
		Bug: This funtion is not recursive. It only works on one level.
		"""
		found_item = -1
		for it in self.items:
			if self.items[it].getName() == item_name:
				found_item = it
				break
			if self.items[it].hasItem(item_name):
				self.items[it].removeItem(item_name)
				return True
		if found_item == -1:
			return False
		del(self.items[found_item])
		return True

	def getItems(self):
		""" Return a dictionary of items contained in the room """
		return self.items

	def printDetails(self):
		"""Print details about the room and everything in it"""
		print(self.getName())
		print("-" * len(self.getName()))
		print(self.getDescription())
		if len(self.items) > 0:
			for it in self.items:
				print((it + ": "))
				self.items[it].printDetails()
		for direction in self.linkedRooms:
			print("The " + self.linkedRooms[direction].getName() + " is " + direction)

	def move(self, direction):
		if direction in self.linkedRooms:
			print("\n")
			return self.linkedRooms[direction]
		else:
			print(">>> You can't go that way\n")
			return self