class Superhero:

    def __init__(self, name, alias, superpower, city):

        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.city = city
    
    def use_power(self):

        print(f"{self.name} ({self.alias}) uses {self.superpower} in {self.city}")
    
    def change_identity(self, new_alias):

        print(f"{self.name} changes identity to {new_alias}")

    def reveal_identity(self):

        print(f"{self.name} is {self.alias}")

    def describe(self):
        
        print(f"{self.alias} is {self.name} possesing {self.superpower} to protect {self.city}")