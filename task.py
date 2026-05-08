class Person:
    name = "Костя"
    age = 15
    def introduce(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років")
hna = Person()        
hna.introduce()