#!/usr/bin/env python3

from classes.ATM import *
from classes.Bank import Bank


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
            info = atm.insert_card(card)
            if info:
                print(info)
        case "2":
            currency, cash = input("enter amount of cash (currency and amount) --- ").split()
            cash = int(cash)
            cash_list = atm.withdraw_money(currency, cash)
            if cash_list:
                print(*cash_list, sep='\n')
        case "3":
            money_dict = atm.show_balance()
            if money_dict:
                for currency, amount in money_dict.items():
                    print(currency, amount)
        case "4":
            phone_number = int(input("input phone number --- "))
            currency, cash = input("enter amount of cash (currency and amount) --- ").split()
            cash = int(cash)
            info = atm.top_up_phone_balance(phone_number, currency, cash)
            if info:
                print(info)
        case "5":
            info = atm.remove_card()
            if info:
                print(info)
        case _:
            return

    working_with_card(atm, card)


def main():
    b_bank = Bank()
    atm = ATM()
    cards = b_bank.create_cards("my_card.txt")
    my_card = cards[0]
    atm.add_money_to_cash_holder({"USD": 1000, "EU": 124})
    print("==================================================")
    working_with_card(atm, my_card)


if __name__ == "__main__":
    main()
