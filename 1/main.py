#!/usr/bin/env python3

from classes.ATM import *
from csv_reader import CSVReader


def working_with_card(atm: ATM, card: Card) -> None:
    func_number = input("choose operation:\n"
                        "1 --- insert card\n"
                        "2 --- withdraw money\n"
                        "3 --- show balance\n"
                        "4 --- top up phone balance\n"
                        "5 --- remove card\n"
                        "6 --- exit\n"
                        )
    match func_number:
        case "1":
            atm.insert_card(card)
        case "2":
            atm.withdraw_money()
        case "3":
            atm.show_balance()
        case "4":
            atm.top_up_phone_balance()
        case "5":
            atm.remove_card()
        case _:
            return

    working_with_card(atm, card)


def main():
    b_bank = Bank()
    atm = ATM()
    CSVReader.read_info(b_bank, "cards_info.csv")
    my_card = b_bank.cards[0]
    # b_bank.add_money_to_atm(atm, {"USD": 1000, "EU": 124})
    # my_card = b_bank.create_card("me", balance={"USD": 13600})
    print("==================================================")
    working_with_card(atm, my_card)


if __name__ == "__main__":
    main()
