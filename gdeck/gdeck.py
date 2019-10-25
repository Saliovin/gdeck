class Card:
    def __init__(self, rank, suit):
        """
        :param rank: Card rank
        :param suit: Card suit
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """
        :return: String equal to '{rank} of {suit}'
        """
        return f'{self.rank} of {self.suit}'


class Deck:
    ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',)
    suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')

    def __init__(self):
        """
        Deck constructor
        """
        self.count = 0
        self.cards = [Card(rank, suit) for rank in Deck.ranks for suit in Deck.suits]

    def __len__(self):
        """
        :return: Integer equal to the size of the Deck
        """
        return len(self.cards)

    def __getitem__(self, index):
        """
        :param index: Position in the list
        :return: Value at the position in the list
        """
        return self.cards[index]

    def __iter__(self):
        """
        :return: Same object instance
        """
        return self

    def __next__(self):
        """
        :return: Next card in the deck
        """
        if self.count < len(self.cards):
            next_card = self.cards[self.count]
        else:
            raise StopIteration

        self.count += 1
        return next_card

    def __repr__(self):
        """
        :return: String equal to the list contents of the deck
        """
        return str(self.cards)
