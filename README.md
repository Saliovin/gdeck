# gdeck

## What is it?
This is a Python module implementing playing cards.

## Requirements
- [Python 3](https://www.python.org/downloads/)

## How to install
```
pip install git+https://github.com/Saliovin/gdeck.git
```
## How to use?
```
>>> import gdeck
```
## Classes

```Card(rank, suit)``` - Creates a Card object with the given parameters as properties.

```Deck()``` - Creates a Deck object cointaining 52 Card objects varying ranks and suits.

## How To Test
Open terminal inside the tests directory
```
pytest --cov
```
