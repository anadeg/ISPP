from unittest import TestCase
from classes.ATM import ATM, Banknote, Card, Bank
from exceptions.CardIsInserted import CardIsInsertedException


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
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        b1._Bank__cards = [c1, c2]
        atm = ATM()
        atm.insert_card(c1)
        self.assertTrue(atm.check_card())

    # def test_withdraw_money(self):
    #     self.fail()

    def test_withdraw_money_1(self):
        b1 = Bank()
        c1 = Card("1111", "me", 1111, {})
        c2 = Card("2222", "not me", 2222, {})
        b1._Bank__cards = [c1]
        atm = ATM()
        atm.insert_card(c2)
        self.assertFalse(atm.withdraw_money("USD", 10))

    # def test_show_balance(self):
    #     self.fail()
    #
    # def test_top_up_phone_balance(self):
    #     self.fail()
    #
    # def test_remove_card(self):
    #     self.fail()
