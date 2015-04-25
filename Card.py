"""
    Monday April 14th, 2014
    CIS 210 Conery Spring
    Cards.py
    Author: Sean Grady
    Class Card is defined to be able to create an interactive card session with a deck of cards and another class blackjack to specify a different type of deck to be created
"""

class Card:
	##storing Card.ranks

    def __init__(self, id):
    	'takes the id of a card and returns a card'
    	self._id = id
    	self._suit, self._rank = divmod(self._id, 13)##this gives the suit and rank integer by id//13 and id%13 defined as a tuple variable
    	self._pt = 0
    	self._sym = ""  ##variable to store the card symbol(letter/num)
    	 #variable to store points value
        ##control statement that assigns a unicode string to represent a suit


    	if self._id > 51 or self._id < 0:
    		print("ID must be a value between 0 and 51")
    	



         
    def __repr__(self):
    	##ranks are written as rank:'card sym'
    	##so ranks[self.pos] gives 'J' where self.pos is = to 9
    	ranks = {
    	        0:'2',
    	        1:'3',
    	        2:'4',
    	        3:'5',
    	        4:'6',
    	        5:'7',
    	        6:'8',
    	        7:'9',
    	        8:'10',
    	        9:'J',
    	        10:'Q',
    	        11:'K',
    	        12:'A'

    	} [self._rank]

    	suits = {

    	        0:"\u2663",
    	        1:"\u2666",
    	        2:"\u2665",
    	        3:"\u2660"

    	} [self._suit]

    	self._sym = ranks##reassign self.sym to use our points definiton
    	

    	return ranks + suits

    def __lt__(self, other):
    	return self._rank < other._rank 

    def rank(self):
    	'returns the letter or number rank of the card'
    	return self._rank

    def suit(self):
    	'returns the suit of the card'
    	return self._suit

    def points(self):
    	'The cards also recieve an amount of points for their face or ace value'
    	ranks = {
    	        0:'2',
    	        1:'3',
    	        2:'4',
    	        3:'5',
    	        4:'6',
    	        5:'7',
    	        6:'8',
    	        7:'9',
    	        8:'10',
    	        9:'J',
    	        10:'Q',
    	        11:'K',
    	        12:'A'
    	} [self._rank]

    	points = {
                 "A":4,
                 "K":3,
                 "Q":2,
                 "J":1,
                 "10":0,
                 "9":0,
                 "8":0,
                 "7":0,
                 "6":0,
                 "5":0,
                 "4":0,
                 "3":0,
                 "2":0,
    	} [ranks]
    	

    	return points

class BlackjackCard(Card):
	'Blackjack class using Card as its base class'

	def __lt__(self,other):
		return self._rank < other._rank

	def points(self):
		'returns a different value for the point of each card in blackjack'

		ranks = {
    	        0:'2',
    	        1:'3',
    	        2:'4',
    	        3:'5',
    	        4:'6',
    	        5:'7',
    	        6:'8',
    	        7:'9',
    	        8:'10',
    	        9:'J',
    	        10:'Q',
    	        11:'K',
    	        12:'A'
    	} [self._rank]



		points = {
                 "A":11,
                 "K":10,
                 "Q":10,
                 "J":10,
                 "10":10,
                 "9":9,
                 "8":8,
                 "7":7,
                 "6":6,
                 "5":5,
                 "4":4,
                 "3":3,
                 "2":2

    	} [ranks]

		self._pt = points
		return self._pt



def new_deck(Class):
    'takes a class and returns a deck of cards using that class'
    return Class(Card)


def points(hand):
	'function points that takes a list of card objects ie [2c 3c 4c] and returns the sum of the points in that hand using the built-in sum function ie that hand would equal 9'
	res = 0
    
	for item in hand:
		res += item.points()
	return res



	