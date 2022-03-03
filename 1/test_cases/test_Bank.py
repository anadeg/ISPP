import unittest
from classes.Bank import Bank, Card


class TestBank(unittest.TestCase):
    def test_cards(self):
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        b1._Bank__cards = [c1, c2]
        self.assertEqual(b1.cards, [c1, c2])

    def test_find_card_1(self):
        b1 = Bank()
        b2 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        c3 = Card("3333", "me", 3333, {})
        c4 = Card("4444", "not me", 4444, {})
        c5 = Card("5555", "not me", 5555, {})
        b1._Bank__cards = [c1, c2, c3]
        b2._Bank__cards = [c4]
        self.assertEqual(Bank.find_card(c5), False)

    def test_find_card_2(self):
        b1 = Bank()
        b2 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        c3 = Card("3333", "me", 3333, {})
        c4 = Card("4444", "not me", 4444, {})
        b1._Bank__cards = [c1, c2, c3]
        b2._Bank__cards = [c4]
        self.assertEqual(Bank.find_card(c4), True)
