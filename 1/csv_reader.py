import csv
import ast

from classes.Bank import Bank


class CSVReader:
    @staticmethod
    def read_info(bank, file_name):
        cards = []
        with open(file_name) as f:
            reader = csv.reader(f, quotechar=';')
            for row in reader:
                card_balance = ast.literal_eval(row[-1])
                new_card = bank.create_card(row[0], card_balance)
                cards.append(new_card)
        return cards


