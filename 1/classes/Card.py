from typing import TypeGuard

from exceptions.CardIsBlocked import CardIsBlockedException


class Card:
    def __init__(self, number: str, name: str, password: int, balance=None) -> None:
        self.__active = True  # blocked from operations or not
        self.number = number
        self.name = name
        self.__password = password
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def password(self):
        return self.__password

    def check_password(self) -> TypeGuard:
        try:
            if not self.__active:
                raise CardIsBlockedException()
        except CardIsBlockedException as error:
            print(error)
            return False

        tryings = 0
        while tryings < 3:
            check = int(input("enter password --- "))
            if check != self.password:
                tryings += 1
                print(f"password was incorrect. {3 - tryings} tryings have left")
            else:
                return True
        self.__active = False
        print("your card was blocked")
        return False

