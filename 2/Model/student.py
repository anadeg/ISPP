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
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"\nname: {self.name}," \
               f"\ngroup: {self.group}," \
               f"\nsick: {self.sick}," \
               f"\nabsence: {self.absence}" \
               f"\nother: {self.other}"
