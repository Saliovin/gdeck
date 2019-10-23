class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',)
        suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.index = 0

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __repr__(self):
        return str(self.cards)
