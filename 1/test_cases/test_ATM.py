from unittest import TestCase
from classes.ATM import ATM, Banknote


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

    # def test_insert_card(self):
    #     self.fail()
    #
    # def test_check_card(self):
    #     self.fail()
    #
    # def test_withdraw_money(self):
    #     self.fail()
    #
    # def test_show_balance(self):
    #     self.fail()
    #
    # def test_top_up_phone_balance(self):
    #     self.fail()
    #
    # def test_remove_card(self):
    #     self.fail()
