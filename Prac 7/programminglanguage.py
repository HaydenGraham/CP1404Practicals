class ProgrammingLaunguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def __str__(self):
        return "{}, {} typing, reflection={}, First appeared in {}"\
            .format(self.name, self.typing, self.reflection, self.year)
