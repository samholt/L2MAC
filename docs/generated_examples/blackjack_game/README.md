# Blackjack CLI Game

This is a simple command-line interface (CLI) Blackjack game where you play against the dealer.

## Installation

First, ensure you have Python installed on your system. This game was developed with Python 3.9, but it should work with most Python 3.x versions.

Then, install the required Python packages by running:

```
pip install -r requirements.txt
```

## Running the Game

To start the game, simply run the following command in your terminal:

```
python blackjack.py
```

Follow the on-screen prompts to play the game. You will be asked whether you want to 'Hit' or 'Stand' during your turn. The goal is to get as close to 21 without going over.

## Rules

- The game is played with a standard deck of 52 cards.
- Aces can be worth 1 or 11 points, face cards (J, Q, K) are worth 10 points, and all other cards are worth their face value.
- The dealer must hit until their cards total 17 or higher.
- If you go over 21, you bust and the dealer wins.
- If the dealer goes over 21, they bust and you win.
- If you have a higher score than the dealer without busting, you win.

Enjoy the game!
