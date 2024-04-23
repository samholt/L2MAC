import json
from copy import deepcopy
from typing import List

from l2mac.tools.code_analysis import (
    check_pytest_with_timeout,
    check_syntax_with_timeout,
    count_errors_in_syntax,
)


def write_files(list_of_file_objects: List[dict] = [], file_dict: dict = {}, enable_tests=True):
    new_file_dict = implement_git_diff_on_file_dict(
        file_dict_input=file_dict, change_files_and_contents_input=list_of_file_objects
    )
    file_dict = new_file_dict
    # Run tests
    # Syntax check
    if not enable_tests:
        output = {"write_files_status": "success", "message": "write_files completed successfully."}
        return json.dumps(output), file_dict
    syntax_results = check_syntax_with_timeout(file_dict)
    if "Manual tests passed" in syntax_results:
        syntax_error_count = 0
    else:
        syntax_error_count = count_errors_in_syntax(syntax_results)
    test_results = check_pytest_with_timeout(file_dict)
    if "Manual tests passed" in test_results:
        test_results = "All tests passed"
    elif "No tests found" in test_results:
        test_results = "All tests passed"
    if "All tests passed" in test_results and syntax_error_count == 0:
        output = {"write_files_status": "success", "message": "All tests passed."}
    else:
        new_output = test_results.strip() + "\n" + syntax_results.strip()
        # if len(new_output) > 5000:
        #     new_output = new_output[:5000]
        #     new_output = new_output + '\nRest of output was trimmed.'
        output = {
            "write_files_status": "success",
            "message": "write_files completed successfully. Test run results: \n"
            + new_output
            + "\n You must fix this code by writing code to complete this sub task step. If a test is failing the error could be the code, or the test is incorrect, so feel free to overwrite and change the tests when they are incorrect, to make all tests pass.",
        }
    return json.dumps(output), file_dict


def implement_git_diff_on_file_dict(file_dict_input: dict, change_files_and_contents_input: []) -> dict:
    """Implement git diff on file_dict, and return the new file_dict.

    Args: file_dict: dict, change_files_and_contents: []

    Returns: dict

    Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
    """
    file_dict = deepcopy(file_dict_input)
    change_files_and_contents = deepcopy(change_files_and_contents_input)
    for obj in change_files_and_contents:
        file_path = obj["file_path"]
        change_file_contents = obj["file_contents"]
        if file_path in file_dict:
            existing_file_contents = file_dict[file_path]
        else:
            existing_file_contents = []
        file_ending = file_path.split(".")[1]
        # new_file_contents = implement_git_diff_on_file_contents(existing_file_contents, change_file_contents, file_type=file_ending, overwrite=obj['overwrite_file'])
        new_file_contents = update_file_contents(existing_file_contents, change_file_contents, file_type=file_ending)
        file_dict[file_path] = new_file_contents
    return file_dict


def update_file_contents(existing_file_contents, change_file_contents, file_type="py") -> [str]:
    """Implement git diff on file_contents, and return the new file_contents.

    Args: existing_file_contents: [str], change_file_contents: [str]

    Returns: [str]

    Description: Adheres to this definition: When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is "+ 1: import time\n+ 2: import os". Editing an existing line is "- 5: apple = 2 + 2\n+ 5: apple = 2 + 3". Deleting a line is "- 5: apple = 2 + 2".
    """
    existing_file_contents = change_file_contents
    return existing_file_contents.split("\n")


def delete_files(files: List[str], file_dict: dict, enable_tests=True):
    for file in files:
        if file == "-1":
            file_dict = {}
        if file in file_dict:
            del file_dict[file]
    output = {"status": "success", "message": "delete_files completed successfully."}
    return json.dumps(output), file_dict


# Write unit tests for the functions above
def test_implement_git_diff_on_file_dict():
    file_dict = {}
    change_files_and_contents = [
        {"file_path": "requirements.txt", "file_contents": "pytest==7.1.2\nflask==2.1.2\n"},
        "file_path:",
        "blackjack/card.py",
        "file_contents:",
        "\"\"\"Defines the Card class for the Blackjack game.\"\"\"\n\n\nclass Card:\n\t\"\"\"Represents a single playing card.\"\"\"\n\n\tdef __init__(self, suit, value):\n\t\t\"\"\"Initialize a new card.\n\n\t\tArgs:\n\t\t\tsuit (str): The suit of the card (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades').\n\t\t\tvalue (str): The value of the card (e.g., '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace').\n\t\t\"\"\"\n\t\tself.suit = suit\n\t\tself.value = value\n\n\tdef __repr__(self):\n\t\treturn f\"{self.value} of {self.suit}\"",
        "file_path:",
        "blackjack/deck.py",
        "file_contents:",
        "\"\"\"Defines the Deck class for the Blackjack game.\"\"\"\n\nfrom .card import Card\nimport random\n\nclass Deck:\n\t\"\"\"Represents a deck of playing cards.\"\"\"\n\n\tdef __init__(self):\n\t\t\"\"\"Initialize a new deck of cards.\"\"\"\n\t\tself.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']]\n\t\trandom.shuffle(self.cards)\n\n\tdef draw_card(self):\n\t\t\"\"\"Draw a card from the deck.\"\"\"\n\t\treturn self.cards.pop()",
        "file_path:",
        "blackjack/hand.py",
        "file_contents:",
        '"""Defines the Hand class for the Blackjack game."""\n\n\nclass Hand:\n\t"""Represents a player\'s or dealer\'s hand in the game."""\n\n\tdef __init__(self):\n\t\t"""Initialize a new hand with no cards."""\n\t\tself.cards = []\n\t\tself.value = 0\n\t\tself.aces = 0\n\n\tdef add_card(self, card):\n\t\t"""Add a card to the hand and adjust the score."""\n\t\tself.cards.append(card)\n\t\tif card.value == \'Ace\':\n\t\t\tself.aces += 1\n\t\tself.adjust_for_ace()\n\n\tdef adjust_for_ace(self):\n\t\t"""Adjust the hand\'s value if an ace is present."""\n\t\twhile self.value > 21 and self.aces:\n\t\t\tself.value -= 10\n\t\t\tself.aces -= 1',
        "file_path:",
        "blackjack/game.py",
        "file_contents:",
        '"""Defines the Game class for the Blackjack game."""\n\nfrom .deck import Deck\nfrom .hand import Hand\n\n\nclass Game:\n\t"""Manages the flow and rules of a Blackjack game."""\n\n\tdef __init__(self):\n\t\t"""Initialize the game with a deck and two hands."""\n\t\tself.deck = Deck()\n\t\tself.player_hand = Hand()\n\t\tself.dealer_hand = Hand()\n\n\tdef deal_cards(self):\n\t\t"""Deal two cards to both player and dealer."""\n\t\tfor _ in range(2):\n\t\t\tself.player_hand.add_card(self.deck.draw_card())\n\t\t\tself.dealer_hand.add_card(self.deck.draw_card())\n\n\tdef player_hit(self):\n\t\t"""Handle player hitting."""\n\t\tself.player_hand.add_card(self.deck.draw_card())\n\t\tif self.player_hand.value > 21:\n\t\t\treturn \'Bust\'\n\t\telse:\n\t\t\treturn \'Continue\'\n\n\tdef player_stand(self):\n\t\t"""Handle player standing."""\n\t\t# Game logic for when player stands\n\n\tdef compare_hands(self):\n\t\t"""Compare the player\'s and dealer\'s hands to determine the winner."""\n\t\t# Logic to determine the winner',
        "file_path:",
        "blackjack/main.py",
        "file_contents:",
        '"""Main script for the CLI Blackjack game."""\n\nfrom .game import Game\n\n\ndef main():\n\t"""Set up and run the Blackjack game."""\n\tgame = Game()\n\t# Game setup and loop logic here\n\nif __name__ == \'__main__\':\n\tmain()',
        "file_path:",
        "tests/test_card.py",
        "file_contents:",
        '"""Unit tests for the Card class in the Blackjack game."""\n\nimport pytest\nfrom blackjack.card import Card\n\n\ndef test_card_initialization():\n\t"""Test that a card is initialized with the correct suit and value."""\n\tcard = Card(\'Hearts\', \'2\')\n\tassert card.suit == \'Hearts\'\n\tassert card.value == \'2\'',
        "file_path:",
        "tests/test_deck.py",
        "file_contents:",
        '"""Unit tests for the Deck class in the Blackjack game."""\n\nimport pytest\nfrom blackjack.deck import Deck\n\n\ndef test_deck_initialization():\n\t"""Test that a deck is correctly initialized with 52 cards."""\n\tdeck = Deck()\n\tassert len(deck.cards) == 52\n\n\ndef test_draw_card():\n\t"""Test that drawing a card from the deck reduces its size by one."""\n\tdeck = Deck()\n\tdeck.draw_card()\n\tassert len(deck.cards) == 51',
        "file_path:",
        "tests/test_hand.py",
        "file_contents:",
        '"""Unit tests for the Hand class in the Blackjack game."""\n\nimport pytest\nfrom blackjack.hand import Hand\nfrom blackjack.card import Card\n\n\ndef test_hand_initialization():\n\t"""Test that a hand is correctly initialized with no cards."""\n\thand = Hand()\n\tassert len(hand.cards) == 0\n\n\ndef test_add_card():\n\t"""Test that adding a card to the hand works correctly."""\n\thand = Hand()\n\thand.add_card(Card(\'Hearts\', \'2\'))\n\tassert len(hand.cards) == 1\n\tassert hand.cards[0].value == \'2\'',
        "file_path:",
        "tests/test_game.py",
        "file_contents:",
        '"""Unit tests for the Game class in the Blackjack game."""\n\nimport pytest\nfrom blackjack.game import Game\n\n\ndef test_game_initialization():\n\t"""Test that the game is initialized with a deck and two hands."""\n\tgame = Game()\n\tassert game.deck\n\tassert game.player_hand\n\tassert game.dealer_hand\n\n\ndef test_deal_cards():\n\t"""Test that dealing cards works correctly."""\n\tgame = Game()\n\tgame.deal_cards()\n\tassert len(game.player_hand.cards) == 2\n\tassert len(game.dealer_hand.cards) == 2',
        "file_path:",
        "tests/conftest.py",
        "file_contents:",
        '"""Configuration file for pytest in the Blackjack game project."""\n\nimport pytest\n\n# Configuration and fixtures for pytest can be added here.',
    ]
    new_file_dict = implement_git_diff_on_file_dict(file_dict, change_files_and_contents)
    assert new_file_dict == {"test.py": ["import time", "import os"]}
    print("All tests passed.")


def test_write_files():
    # Test write_files
    files_and_contents = [{"file_path": "test.py", "file_contents": "+ 1: import time\n+ 2: import os"}]
    file_dict = {}
    output, file_dict = write_files(files_and_contents, file_dict)
    assert output == '{"write_files_status": "success", "message": "All tests passed."}'
    assert file_dict == {"test.py": ["import time", "import os"]}
    # Test implement_git_diff_on_file_dict
    file_dict = {}
    change_files_and_contents = [{"file_path": "test.py", "file_contents": "+ 1: import time\n+ 2: import os"}]
    file_dict = implement_git_diff_on_file_dict(file_dict, change_files_and_contents)
    assert file_dict == {"test.py": ["import time", "import os"]}
    # Test update_file_contents
    existing_file_contents = "import time\nimport os"
    change_file_contents = "+ 1: import time\n+ 2: import os"
    new_file_contents = update_file_contents(existing_file_contents, change_file_contents)
    assert new_file_contents == ["import time", "import os"]
    # Test delete_files
    files = ["test.py"]
    file_dict = {"test.py": ["import time", "import os"]}
    output, file_dict = delete_files(files, file_dict)
    assert output == '{"status": "success", "message": "delete_files completed successfully."}'
    assert file_dict == {}
    # Test delete_files with -1
    files = ["-1"]
    file_dict = {"test.py": ["import time", "import os"]}
    output, file_dict = delete_files(files, file_dict)
    assert output == '{"status": "success", "message": "delete_files completed successfully."}'
    assert file_dict == {}
    # Test delete_files with file not in file_dict
    files = ["test.py"]
    file_dict = {}
    output, file_dict = delete_files(files, file_dict)
    assert output == '{"status": "success", "message": "delete_files completed successfully."}'
    assert file_dict == {}
    print("All tests passed.")
