from .character import Character


class Enemy(Character):

	def __init__(self, en_name, en_descr, en_state="sleeping", en_resilience=1):
		super(Character, self).__init__(en_name, en_descr, en_state)
		self.resilience = en_resilience
		self.fight_responses = {}

	def addFightResponse(self, method, response):
		self.fight_responses[method] = response

	def fight(self, method):
		self.speak("Really?")
		if method in self.fight_responses.keys():
			self.fight_responses[method](method)
			return 0
		else:
			self.speak("Using a " + method + " on me is doomed to fail, cretin.")
			self.setState("Irritated")
		return 1
