from typing import TypeGuard, Dict


class Card:
    def __init__(self, number: str, name: str, password: int, balance=None) -> None:
        self.__active = True  # blocked from operations or not
        self.number = number
        self.name = name
        self.__password = password
        self.__balance = balance

    @property
    def balance(self) -> Dict[str, int]:
        return self.__balance

    @property
    def password(self) -> int:
        return self.__password

    @property
    def active(self) -> TypeGuard:
        return self.__active

    def check_password(self) -> TypeGuard:
        attempts = 0
        while attempts < 3:
            check = int(input("enter password --- "))
            if check != self.__password:
                attempts += 1
                print(f"password was incorrect. {3 - attempts} attempts have left")
            else:
                return True
        self.__active = False
        print("YOUR CARD WAS BLOCKED")
        return False
