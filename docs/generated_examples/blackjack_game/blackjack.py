import random


# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self):
        return {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }[self.rank]


# Define the Deck class
class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            for rank in [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
        ]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "A":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Define the Game class
class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        print("Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.show_hands()
        self.player_turn()
        self.dealer_turn()
        self.show_result()

    def player_turn(self):
        while input("Hit or Stand? (h/s): ").lower() == "h":
            self.player_hand.add_card(self.deck.deal_card())
            self.player_hand.adjust_for_ace()
            self.show_hands()
            if self.player_hand.value > 21:
                print("Player busts!")
                return
        self.dealer_turn()

    def dealer_turn(self):
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_hand.adjust_for_ace()

    def show_hands(self):
        print("Player's Hand:", *[f"{card.rank} of {card.suit}" for card in self.player_hand.cards])
        print("Dealer's Hand:", *[f"{card.rank} of {card.suit}" for card in self.dealer_hand.cards[:1]], "and [HIDDEN]")

    def show_result(self):
        self.adjust_final_hands()
        print("Final Hands:")
        self.show_hands()
        if self.player_hand.value > 21:
            print("Dealer wins!")
        elif self.dealer_hand.value > 21 or self.player_hand.value > self.dealer_hand.value:
            print("Player wins!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def adjust_final_hands(self):
        self.player_hand.adjust_for_ace()
        self.dealer_hand.adjust_for_ace()


if __name__ == "__main__":
    game = Game()
    game.start_game()
