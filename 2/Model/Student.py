class Student:
    def __init__(self, name, group, sick, absence, other):
        self.name = name
        self.group = group
        self.sick = sick
        self.absence = absence
        self.other = other

    def __gt__(self, other):
        return self.name > other.name

    def __lt__(self, other):
        return not __gt__(other)

    def __eq__(self, other):
        return self.name == other.name
