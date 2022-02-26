from random import randint
from typing import Dict

from .Card import Card
try:
    from .ATM import ATM
except ImportError:
    import sys
    ATM = sys.modules[__package__ + '.ATM']


from exceptions.CardDoesNotExist import CardDoesNotExistException


class Bank:
    banks_list = []

    def __init__(self):
        self.__cards = []
        Bank.banks_list.append(self)

    def __del__(self):
        Bank.banks_list.remove(self)

    @property
    def cards(self):
        return self.__cards

    @staticmethod
    def add_money_to_atm(atm: ATM, money: Dict[str, int]) -> None:
        for nominal, amount in money.items():
            if nominal not in atm.cash_holder:
                atm.cash_holder[nominal] = amount
            else:
                atm.cash_holder[nominal] += amount

    def create_card(self, user_name: str, balance=None) -> Card:
        password = randint(1000, 9999)
        number = " ".join([str(randint(1000, 9999)) for _ in range(4)])
        new_card = Card(number, user_name, password, balance)
        self.__cards.append(new_card)

        print(f"your password is: {password}. please, don't forget it")
        return new_card

    @classmethod
    def find_card(cls, card: Card):
        banks_cards = []
        for bank in cls.banks_list:
            banks_cards.extend(bank.cards)
        try:
            if card not in banks_cards:
                raise CardDoesNotExistException()
        except CardDoesNotExistException as error:
            print(error)
            return False
        return True
