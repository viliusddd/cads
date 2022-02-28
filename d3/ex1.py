# Sukurti norimą sąrašą ir žodyną ir juose:
# • Atspausdinti vieną norimą įrašą
# • Pridėti įrašą
# • Ištrinti įrašą
# • pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(),
# remove…

names = ['Vilius', 'Jonas', 'Petras']

names.append('Birute')  # Pridėti įrašą
print(names)

names.pop(1)  # Ištrinti įrašą
print(names)

names[0] = 'Andrius'  # pakeisti įrašą
print(names)
print('\n')

amount = {
    'cat': 5,
    'dog': 6,
    'horse': 15
}

amount['chicken'] = 3  # Pridėti įrašą
print(amount)

amount.pop('dog')  # Ištrinti įrašą
print(amount)

amount['horse'] = {'white': 3, 'brown': 12}
print(amount)
