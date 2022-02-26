class CardDoesNotExistException(Exception):
    def __init__(self, *args):
        if args:
            self.massage = args[0]
        else:
            self.massage = "CARD DOES NOT EXIST"

    def __str__(self):
        return self.massage
