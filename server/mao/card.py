
from enum import Enum
import random

class CardType (Enum):
    VALUE_ACE = "ace"
    VALUE_TWO = "two"
    VALUE_THREE = "three"
    VALUE_FOUR = "four"
    VALUE_FIVE = "five"
    VALUE_SIX = "six"
    VALUE_SEVEN = "seven"
    VALUE_EIGHT = "eight"
    VALUE_NINE = "nine"
    VALUE_TEN = "ten"
    VALUE_JACK = "jack"
    VALUE_QUEEN = "queen"
    VALUE_KING = "king"
    VALUE_JOKER = "joker"

    SUITE_SPADES = "spades"
    SUITE_HEARTS = "hearts"
    SUITE_CLUBS = "clubs"
    SUITE_DIAMONDS = "diamonds"

    COLOR_RED = "red"
    COLOR_BLACK = "black"

    ANY = "any"
    DEFAULT = ""

CardValues = [
    CardType.VALUE_ACE,
    CardType.VALUE_TWO,
    CardType.VALUE_THREE,
    CardType.VALUE_FOUR,
    CardType.VALUE_FIVE,
    CardType.VALUE_SIX,
    CardType.VALUE_SEVEN,
    CardType.VALUE_EIGHT,
    CardType.VALUE_NINE,
    CardType.VALUE_TEN,
    CardType.VALUE_JACK,
    CardType.VALUE_QUEEN,
    CardType.VALUE_KING,
]

CardValuesWithJoker = CardValues + [CardType.VALUE_JOKER]

CardSuites = [
    CardType.SUITE_SPADES,
    CardType.SUITE_HEARTS,
    CardType.SUITE_CLUBS,
    CardType.SUITE_DIAMONDS,
]

class Card:
    """
    A standard playing card.
    """

    def __init__ (self, value, suite):
        # value and suite are instances of the enum CardType
        self.value = value
        self.suite = suite

    def __str__ (self):
        if self.value == CardType.VALUE_JOKER:
            return "joker"
        else:
            return "{} of {}".format(str(self.value), str(self.suite))

    def matchType (self, cardType)
        """
        Return True if this card matches a CardType.
        """
        if cardType == CardType.ANY:
            return True
        elif cardType == CardType.DEFAULT:
            return False
        elif (cardType == CardType.COLOR_RED and
            self.suite in [CardType.SUITE_HEARTS, CardType.SUITE_DIAMONDS]):
            return True
        elif (cardType == CardType.COLOR_BLACK and
            self.suite in [CardType.SUITE_SPADES, CardType.SUITE_CLUBS]):
            return True
        elif cardType == self.suite:
            return True
        elif cardType == self.value:
            return True
        else:
            return False




class Deck:
    """
    An ordered list of cards.
    """

    def __init__ (self, cards=None, jokers=0)
        if not cards:
            cards = self.makeStandard52(jokers)
        self.cards = cards

    def makeStandard52 (self, jokers=0):
        """
        Create a standard 52-card deck.
        """
        cards = []
        for suite in CardSuites:
            for value in CardValues:
                cards.append(Card(value, suite))
        for i in range(0, jokers):
            cards.append(Card(CardType.VALUE_JOKER, CardType.DEFAULT))
        return cards

    def shuffle (self):
        random.shuffle(self.cards)

    def draw (self):
        return self.cards.pop()

    def add (self, card):
        self.cards.append(card)


