from typing import List, TypeGuard

from .Bank import Bank
from .Banknote import Banknote
from .Card import Card

from exceptions.CardIsNotInserted import CardIsNotInsertedException
from exceptions.CardIsInserted import CardIsInsertedException
from exceptions.NoSuchCurrency import NoSuchCurrencyException
from exceptions.NotEnoughMoneyOnBalance import NotEnoughMoneyOnBalanceException
from exceptions.NotEnoughMoneyInATM import NotEnoughMoneyInATMException


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

    def insert_card(self, card: Card) -> None:
        try:
            if self.inserted_card is not None:
                raise CardIsInsertedException()
        except CardIsInsertedException as error:
            print(error)
            return

        self.inserted_card = card
        print("your card was successfully inserted")

    def check_card(self) -> TypeGuard:
        try:
            if self.inserted_card is None:
                raise CardIsNotInsertedException()
        except CardIsNotInsertedException as error:
            print(error)
            return False
        return Bank.find_card(self.inserted_card)

    def withdraw_money(self) -> None:   # снять деньги
        if not self.check_card():
            return
        if not self.inserted_card.check_password():
            return

        currency, cash = input("enter amount of cash (currency and amount) --- ").split()
        cash = int(cash)

        try:
            if currency not in self.inserted_card.balance.keys() or currency not in self.__cash_holder.keys():
                raise NoSuchCurrencyException()
        except NoSuchCurrencyException as error:
            print(error)
            return

        try:
            if self.inserted_card.balance[currency] < cash:
                raise NotEnoughMoneyOnBalanceException()
        except NotEnoughMoneyOnBalanceException as error:
            print(error)
            return

        try:
            if self.__cash_holder[currency] < cash:
                raise NotEnoughMoneyInATMException()
        except NotEnoughMoneyInATMException as error:
            print(error)
            return

        self.inserted_card.balance[currency] -= cash
        self.__cash_holder[currency] -= cash

        res = ATM.give_cash(currency, cash)
        print(*res, sep='\n')
        return

    def show_balance(self) -> None:
        if not self.check_card():
            return
        if not self.inserted_card.check_password():
            return
        for currency, amount in self.inserted_card.balance.items():
            print(f"{currency} {amount}")

    def top_up_phone_balance(self) -> None:
        if not self.check_card():
            return
        if not self.inserted_card.check_password():
            return

        phone_number = int(input("input phone number --- "))

        currency, cash = input("enter amount of cash --- ").split()
        cash = int(cash)

        try:
            if currency not in self.inserted_card.balance.keys():
                raise NoSuchCurrencyException()
        except NoSuchCurrencyException as error:
            print(error)
            return

        try:
            if self.inserted_card.balance[currency] < cash:
                raise NotEnoughMoneyOnBalanceException()
        except NotEnoughMoneyOnBalanceException as error:
            print(error)
            return

        self.inserted_card.balance[currency] -= cash
        print(f"you successfully have topped up {phone_number}")

    def remove_card(self) -> None:
        try:
            if self.inserted_card is None:
                raise CardIsNotInsertedException()
        except CardIsNotInsertedException as error:
            print(error)
            return

        self.inserted_card = None
