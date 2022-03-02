import ast


class FileReader:
    @staticmethod
    def read_from_file(file_name: str):
        names = []
        balances = []
        with open(file_name) as file:
            lines = file.readlines()

        for line in lines:
            name, balance = line.split(';')
            names.append(name)
            balance_dict = ast.literal_eval(balance)
            balances.append(balance_dict)

        return names, balances


