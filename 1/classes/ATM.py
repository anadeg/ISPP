from typing import List, TypeGuard, Dict

from .Bank import Bank
from .Banknote import Banknote
from .Card import Card

from exceptions.CardIsNotInserted import CardIsNotInsertedException
from exceptions.CardIsInserted import CardIsInsertedException
from exceptions.NoSuchCurrency import NoSuchCurrencyException
from exceptions.NotEnoughMoney import NotEnoughMoneyException


class ATM:
    def __init__(self):
        self.__cash_holder = {}
        self.inserted_card = None

    @property
    def cash_holder(self):
        return self.__cash_holder

    @staticmethod
    def give_cash(currency: str, how_much: int) -> List[Banknote]:
        nominal_values = [100, 50, 25, 10, 5, 1]
        result = []
        for nominal in nominal_values:
            if nominal <= how_much:
                amount_of_banknotes = how_much // nominal
                for _ in range(amount_of_banknotes):
                    result.append(Banknote(currency, nominal))
                how_much -= amount_of_banknotes * nominal
        return result

    def add_money_to_cash_holder(self, money: Dict[str, int]) -> None:
        for nominal, amount in money.items():
            if nominal not in self.__cash_holder:
                self.__cash_holder[nominal] = amount
            else:
                self.__cash_holder[nominal] += amount

    def insert_card(self, card: Card) -> str:
        try:
            if self.inserted_card is not None:
                raise CardIsInsertedException()
        except CardIsInsertedException as error:
            return error.massage

        self.inserted_card = card
        return "your card was successfully inserted"

    def check_card(self) -> TypeGuard:
        try:
            if self.inserted_card is None:
                raise CardIsNotInsertedException()
        except CardIsNotInsertedException as error:
            print(error)
            return False
        return Bank.find_card(self.inserted_card)

    def withdraw_money(self, currency, cash) -> List[Banknote]:
        if not self.check_card():
            return []
        if not self.inserted_card.check_password():
            return []

        try:
            if currency not in self.inserted_card.balance.keys():
                raise NoSuchCurrencyException("YOU DO NOT HAVE SUCH CURRENCY ON THE CARD")
        except NoSuchCurrencyException as error:
            print(error)
            return []

        try:
            if currency not in self.__cash_holder.keys():
                raise NoSuchCurrencyException("WE DO NOT HAVE SUCH CURRENCY IN THE ATM")
        except NoSuchCurrencyException as error:
            print(error)
            return []

        try:
            if self.inserted_card.balance[currency] < cash:
                raise NotEnoughMoneyException("NOT ENOUGH MONEY ON YOUR CARD")
        except NotEnoughMoneyException as error:
            print(error)
            return []

        try:
            if self.__cash_holder[currency] < cash:
                raise NotEnoughMoneyException("NOT ENOUGH MONEY IN THE ATM")
        except NotEnoughMoneyException as error:
            print(error)
            return []

        self.inserted_card.balance[currency] -= cash
        self.__cash_holder[currency] -= cash

        res = ATM.give_cash(currency, cash)
        return res

    def show_balance(self) -> Dict[str, int]:
        if not self.check_card():
            return {}
        if not self.inserted_card.check_password():
            return {}
        return self.inserted_card.balance

    def top_up_phone_balance(self, phone_number, currency, cash) -> str:
        if not self.check_card():
            return ""
        if not self.inserted_card.check_password():
            return ""

        try:
            if currency not in self.inserted_card.balance.keys():
                raise NoSuchCurrencyException("YOU DO NOT HAVE SUCH CURRENCY ON THE CARD")
        except NoSuchCurrencyException as error:
            return error.massage

        try:
            if self.inserted_card.balance[currency] < cash:
                raise NotEnoughMoneyException("NOT ENOUGH MONEY ON YOUR CARD")
        except NotEnoughMoneyException as error:
            return error.massage

        self.inserted_card.balance[currency] -= cash
        return f"you successfully have topped up {phone_number}"

    def remove_card(self) -> str:
        try:
            if self.inserted_card is None:
                raise CardIsNotInsertedException()
        except CardIsNotInsertedException as error:
            return error.massage

        self.inserted_card = None
        return "your card was removed"
