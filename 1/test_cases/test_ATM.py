from unittest import TestCase

from classes.ATM import ATM, Banknote, Card, Bank
from exceptions.CardIsInserted import CardIsInsertedException
from exceptions.CardIsNotInserted import CardIsNotInsertedException



class TestATM(TestCase):
    def test_give_cash(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"USD": 100})
        amount_list = [50, 10, 1, 1]
        currency = "USD"
        cash_list = []
        for amount in amount_list:
            cash_list.append(Banknote(currency, amount))
        self.assertTrue(atm.give_cash(currency, 62) == cash_list)

    def test_add_money_ATM(self):
        atm = ATM()
        money = {"USD": 1980, "EU": 165}
        atm.add_money_to_cash_holder(money)
        self.assertEqual(atm.cash_holder, money)

    def test_insert_card_1(self):
        atm = ATM()
        c1 = Card("1111", "me", 1111, {})
        self.assertEqual(atm.insert_card(c1), "your card was successfully inserted")

    def test_insert_card_2(self):
        atm = ATM()
        c1 = Card("1111", "me", 1111, {})
        atm.inserted_card = c1
        c2 = Card("2222", "not me", 2222, {})
        e = CardIsInsertedException()
        self.assertEqual(atm.insert_card(c2), e.massage)

    def test_check_card_1(self):
        atm = ATM()
        self.assertFalse(atm.check_card())

    def test_check_card_2(self):
        atm = ATM()
        c1 = Card("1111", "me", 1111, {})
        c1._Card__active = False
        atm.insert_card(c1)
        self.assertFalse(atm.check_card())

    def test_check_card_3(self):
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        b1._Bank__cards = [c2]
        atm = ATM()
        atm.insert_card(c1)
        self.assertFalse(atm.check_card())

    def test_withdraw_money_1(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"EU": 1000})
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertFalse(atm.withdraw_money("EU", 10))

    def test_withdraw_money_2(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"EU": 1000})
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertFalse(atm.withdraw_money("USD", 10))

    def test_withdraw_money_3(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"USD": 1000})
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertFalse(atm.withdraw_money("USD", 500))

    def test_withdraw_money_4(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"USD": 100})
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 1000})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertFalse(atm.withdraw_money("USD", 500))

    def test_withdraw_money_5(self):
        atm = ATM()
        atm.add_money_to_cash_holder({"USD": 1000})
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.withdraw_money("USD", 10), [Banknote("USD", 10)])

    def test_show_balance(self):
        atm = ATM()
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100, "EU": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.show_balance(), {"USD": 100, "EU": 100})

    def test_top_up_phone_balance_1(self):
        atm = ATM()
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100, "EU": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.top_up_phone_balance("99999", "TR", 10), "YOU DO NOT HAVE SUCH CURRENCY ON THE CARD")

    def test_top_up_phone_balance_2(self):
        atm = ATM()
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100, "EU": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.top_up_phone_balance("99999", "EU", 1000), "NOT ENOUGH MONEY ON YOUR CARD")

    def test_top_up_phone_balance_3(self):
        atm = ATM()
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100, "EU": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.top_up_phone_balance("99999", "EU", 50), "you successfully have topped up 99999")

    def test_remove_card_1(self):
        atm = ATM()
        e = CardIsNotInsertedException()
        self.assertEqual(atm.remove_card(), e.massage)

    def test_remove_card_2(self):
        atm = ATM()
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {"USD": 100, "EU": 100})
        b1._Bank__cards = [c1]
        atm.insert_card(c1)
        self.assertEqual(atm.remove_card(), "your card was removed")
