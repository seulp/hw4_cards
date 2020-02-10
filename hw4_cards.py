import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        # Test that if you create a card with rank 12, its rank_name will be "Queen"
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_Clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_king_of_spade(self):
        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), "King of Spades")

    def test_4_deck(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_5_deckcard(self):
        deck = cards.Deck()
        # Check last card of deck(specific)
        card_from_deck = deck.deal_card()
        self.assertEqual(card_from_deck.__str__(), "King of Spades")
        # Check the type of card(general)
        new_card = cards.Card()
        self.assertEqual(type(card_from_deck), type(new_card))

    def test_6_decklen(self):
        deck = cards.Deck()
        original_len = len(deck.cards)
        _ = deck.deal_card()
        new_len = len(deck.cards)

        self.assertEqual(original_len-1, new_len)

    def test_7_replace(self):
        deck = cards.Deck()
        origianl_len =  len(deck.cards) # 52
        card = deck.deal_card()
        deck.replace_card(card)
        new_len = len(deck.cards) # 51 -> 52

        self.assertEqual(origianl_len, new_len)

    def test_8_already(self):
        deck = cards.Deck()
        original_len = len(deck.cards) # 52

        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), deck.cards[-1].__str__()) # Check the card in the deck

        deck.replace_card(card)
        new_len = len(deck.cards)

        self.assertEqual(original_len, new_len)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
