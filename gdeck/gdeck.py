class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',)
    suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')

    def __init__(self):
        self.count = 0
        self.cards = [Card(rank, suit) for rank in Deck.ranks for suit in Deck.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.cards):
            next_card = self.cards[self.count]
        else:
            raise StopIteration

        self.count += 1
        return next_card

    def __repr__(self):
        return str(self.cards)
