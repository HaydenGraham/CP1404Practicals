class Guitar:

    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        
    def is_vintage(self):
        if self.year >= "1976":
            vintage = "True"
            return vintage
        else:
            vintage = "False"
            return vintage

    def get_age(self):
        self.age = 2017 - self.year
        return self.age


    def __str__(self):
        return "{} ({}) : ${}"\
            .format(self.name, self.year, self.cost)