class CardIsNotInsertedException(Exception):
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = "CARD IS NOT INSERTED"

    def __str__(self):
        return self.massage
