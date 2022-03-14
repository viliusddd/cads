# Sukurti programą, kuri:
# • Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# • Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių
# • Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# • Įdėti sukurtus Zmogus objektus į naują sąrašą
# • Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių
# (ir atbulai)
# Patarimai:
# • Naudoti sorted, attrgetter, reverse, funkciją __repr__
# • from operator import attrgetter

# • Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# • Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f'{self.vardas}, {self.amzius}')

print(repr(people))

# • Inicijuoti kelis Zmogus objektus su vardais ir amžiais
john = Zmogus("John Smith", 55)
lee = Zmogus("Lee Young", 33)
barbara = Zmogus("Barbara", 45)

# • Įdėti sukurtus Zmogus objektus į naują sąrašą
people = [john, lee, barbara]

# • Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
from operator import attrgetter

print(sorted(people, key=attrgetter('vardas')))
print(sorted(people, key=attrgetter('amzius')))

print(sorted(people, key=attrgetter('vardas'), reverse=True))
print(sorted(people, key=attrgetter('amzius'), reverse=True))
