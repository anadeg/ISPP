class NoSuchCurrencyException(Exception):
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = "NO SUCH CURRENCY"

    def __str__(self):
        return self.massage
