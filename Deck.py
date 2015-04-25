"""
	April 21, 2014 CIS 211 John Conery
	Author: Sean Grady
	Decks.py initializes a deck of cards to be shuffled and dealt
	Help from John Conery
"""


from Card import *
from random import shuffle
class Deck(list):
	'creates an instance of a deck, inheriting from the list attrributes which fits the situation'

	hand = []


	def __init__(self):
		'initializes a deck of cards'

		##creating an isa relationship rather than hasa
		list.__init__(self, [Card(i) for i in range(52)])

	def deal(self, num):
		'takes a specfied num and deals the card ie go fish the players are dealt 7 cards'
		
		
		for i in range(5):
			(Deck.hand).append(self.pop())

		return Deck.hand


	def shuffle(self):
		return shuffle(self)

	def restore(self, a):
		'restores a list of card a (usually being the list of cards that have already been removed)'


		for card in a:
			self.append(card)

    

class PinochleDeck(Deck):
	''
	##we want our constructor to inherit attributes from Deck, but specfics must also be applied for a correct pinochle deck
	def __init__(self):
		
		for i in range(52):
			if i%13 > 6:
				self.append(Card(i))
				self.append(Card(i))









