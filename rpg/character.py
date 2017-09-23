from .item import Item
from random import *


class Character(Item):
	magic_word = "joke"

	def __init__(self, character_name, character_description, character_state="pondering"):
		super(Character, self).__init__(character_name, character_description, character_state)
		self.addResponse("hello", self.sayHello)

	def sayHello(self, stimuli):
		self.speak(stimuli + " yourself, stranger")

	def canSpeak(self):
		return True

	def speak(self, words):
		""" The preferred method for Character utterances."""
		print(("\n" + self.getName() + ": <" + words + ">"))

	def fight(self, method):
		print(("\n***" + self.getName() + " is a lover, not a fighter ***"))
		return 0

	def respondTo(self, stimuli):
		""" When the user types
		say name stimuli
		at the prompt, this funtion gets called with stimuli as argument.
		Look through all the responses that have been added with addResponse()
		If a match is found, call the value as a function with stimuli as argument.
		Example for a character named "Dave" whose instance variable is dave:
			def shoot(stimuli):
				print("Dave draws his gun and fires. Bang. Bang. Bang.")
			dave.addResponse("shoot", shoot)
			If not stimuli match is found, say hello
		If this character is Dead, utter a ghostly moan"""
		if self.state == "Dead":
			print(("\n*** The ghost of " + self.name + " moans ***"))
		else:
			if stimuli in self.responses.keys():
				self.responses[stimuli](stimuli)
			else:
				self.sayHello(stimuli)
