from gdeck import gdeck
from random import choice
import pytest


def test_card_class():
    test_card = gdeck.Card("Ace", "Hearts")
    assert (test_card.rank, test_card.suit) == ("Ace", "Hearts")


def test_card_str():
    test_card = gdeck.Card("Ace", "Hearts")
    assert str(test_card) == "Ace of Hearts"


def test_deck_class_contents():
    test_deck = gdeck.Deck()
    assert all(isinstance(card, gdeck.Card) for card in test_deck.cards)


def test_deck_class_size():
    test_deck = gdeck.Deck()
    assert len(test_deck) == 52


def test_deck_choice():
    assert isinstance(choice(gdeck.Deck()), gdeck.Card)


def test_deck_next():
    assert isinstance(next(gdeck.Deck()), gdeck.Card)


def test_deck_stop_iter():
    with pytest.raises(StopIteration):
        test = gdeck.Deck()
        for i in iter(gdeck.Deck()):
            next(test)
        next(test)


def test_deck_str():
    assert str(gdeck.Deck()) == "[Ace of Clubs, Ace of Spades, Ace of Hearts, Ace of Diamonds, 2 of Clubs, " \
                                "2 of Spades, 2 of Hearts, 2 of Diamonds, 3 of Clubs, 3 of Spades, 3 of Hearts, " \
                                "3 of Diamonds, 4 of Clubs, 4 of Spades, 4 of Hearts, 4 of Diamonds, 5 of Clubs, 5 " \
                                "of Spades, 5 of Hearts, 5 of Diamonds, 6 of Clubs, 6 of Spades, 6 of Hearts, " \
                                "6 of Diamonds, 7 of Clubs, 7 of Spades, 7 of Hearts, 7 of Diamonds, 8 of Clubs, " \
                                "8 of Spades, 8 of Hearts, 8 of Diamonds, 9 of Clubs, 9 of Spades, 9 of Hearts, " \
                                "9 of Diamonds, 10 of Clubs, 10 of Spades, 10 of Hearts, 10 of Diamonds, " \
                                "Jack of Clubs, Jack of Spades, Jack of Hearts, Jack of Diamonds, Queen of Clubs, " \
                                "Queen of Spades, Queen of Hearts, Queen of Diamonds, King of Clubs, King of Spades, " \
                                "King of Hearts, King of Diamonds]"
