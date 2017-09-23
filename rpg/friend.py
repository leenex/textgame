from .character import Character


class Friend(Character):

	def __init__(self, en_name, en_descr, en_state="smiling"):
		super(Character, self).__init__(en_name, en_descr, en_state)
		self.addResponse("joke", lambda x: (self.speak("A joke can actually kill people, you know")))

	def fight(self, method):
		self.speak("Don't be a covfefe. I'm supposed to be your friend, mate")
		return 0
