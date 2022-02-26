class NoSuchCurrencyException(Exception):
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = "YOU DO NOT HAVE SUCH CURRENCY ON THE CARD"

    def __str__(self):
        return self.massage
