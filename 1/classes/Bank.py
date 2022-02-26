from random import randint
from typing import Dict, List, TypeGuard

from .Card import Card
from .FileReader import FileReader
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

    def create_cards(self, cards_info) -> List[Card]:
        names, balances = FileReader.read_from_file(cards_info)
        cards_list = []
        for user, balance in zip(names, balances):
            password = randint(1000, 9999)
            number = " ".join([str(randint(1000, 9999)) for _ in range(4)])
            card = Card(number, user, password, balance)
            self.__cards.append(card)
            cards_list.append(card)
            print(f"your password is: {password}. please, don't forget it")
        return cards_list

    @classmethod
    def find_card(cls, card: Card) -> TypeGuard:
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
