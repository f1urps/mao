


# IF (condition)
# AND (condition) AND (condition) ...
# OR (condition) OR (condition) ...
# THEN (consequent)
# AND (consequent) AND (consequent) ...


class RuleEncoding:
    """
    An encoded form of a rule.
    """

    def __init__ (self):
        self.if_condition = None        # Condition
        self.extra_conditions = []      # [("AND", Condition), ("OR", Condition), ... ]
        self.then_consequent = None     # Consequent
        self.extra_consequents = []     # [("AND", Consequent), ("OR", Consequent), ... ]



class Condition:
    """
    A condition for a rule. Must refer to game state and return true/false.
    """

    def evaluate (self, game):
        """
        Return two values:
        * boolean to indicate rule activation, depending on game state
        * dict of instantiated variables
        """
        raise NotImplementedError ("evaluate method must be implemented by a base class.")


class IsPlayedCondition (Condition):
    """
    Detects if the last card played matches a card type.
    e.g. ([ace] is played)
         ([C] is played)
    """

    def __init__ (self, cardType, variable=None):
        self.cardType = cardType    # type of card to check for, or None if variable
        self.variable = variable    # variable name e.g. "C", or None

    def __str__ (self):
        return "[{}] is played".format(str(self.cardType))

    def evaluate (self, game):
        # game.lastMove may be None if the current player didn't play
        activated = (game.lastMove is not None and
                    game.lastMove.matchType(self.cardType)
        return activated, {}


class LastNCardsCondition (Condition):
    """
    Detects if the last N cards prior to the last move match a card type.
    e.g. (last [3] cards are [seven])
         (last [N] cards are [face])
    """

    def __init__ (self, n, cardType, variable=None):
        self.n = n                  # number of cards to check, or None if variable
        self.cardType = cardType    # type of card to check for
        self.variable = variable    # variable name e.g. "N", or None

    def __str__ (self):
        return "last [{}] cards are [{}]".format(
                self.n if self.n else self.variable, str(self.cardType))

    def evaluate (self, game):
        count = self.countStreak(game)
        if self.n:
            return count >= self.n, {}
        else:
            return True, {self.variable: count}

    def countStreak (self, game):
        count = 0
        # Stack is stored in chronological order
        # Start at second-to-last element and iterate backwards,
        # to get recent moves first
        for card in game.stack[-2::-1]:
            if card.matchType(self.cardType):
                count += 1
            else:
                # As soon as we reach a non-matching card, stop counting
                break
        return count

class PriorCardCondition (Condition):
    """
    Detects if the card at a certain position matches a card type.
    e.g. (card [1] prior is [two])
    """

    def __init__ (self, n, cardType):
        self.n = n
        self.cardType = cardType


    def __str__ (self):
        return "card [{}] prior is [{}]".format(
                self.n, str(self.cardType))

    def evaluate (self, game):
        return game.stack[-self.n - 1]





