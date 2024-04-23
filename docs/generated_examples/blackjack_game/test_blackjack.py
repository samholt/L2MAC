from blackjack import Card, Deck, Game, Hand


def test_card_value():
    assert Card("Hearts", "2").value == 2
    assert Card("Hearts", "A").value == 11


def test_deck_deal_card():
    deck = Deck()
    assert isinstance(deck.deal_card(), Card)
    assert len(deck.cards) == 51


def test_hand_add_card_and_value():
    hand = Hand()
    hand.add_card(Card("Hearts", "2"))
    hand.add_card(Card("Hearts", "3"))
    assert hand.value == 5
    assert hand.aces == 0
    hand.add_card(Card("Hearts", "A"))
    assert hand.value == 16
    assert hand.aces == 1


def test_game_flow():
    game = Game()
    # Mocking the player and dealer turns to simulate game flow without user input
    game.player_turn = lambda: None
    game.dealer_turn = lambda: None
    game.start_game()
    # Assuming the game starts with two cards each for player and dealer
    assert len(game.player_hand.cards) == 2
    assert len(game.dealer_hand.cards) == 2
    # Adjusting for ace should be tested in a scenario where it affects the outcome
    hand = Hand()
    hand.add_card(Card("Hearts", "A"))
    hand.add_card(Card("Hearts", "9"))
    hand.add_card(Card("Hearts", "2"))  # Total would be 22, but ace adjustment should bring it to 12
    hand.adjust_for_ace()
    assert hand.value == 12
