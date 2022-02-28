# Sukurti programą, kuri:
# • leistų vartotojui įvesti metus
# • Atspausdintų „Keliamieji metai“, jei taip yra
# • Atspausdintų „Nekeliamieji metai“, jei taip yra

from calendar import isleap

year = int(input('Input year number: '))

if isleap(year):
    print('Keliamieji metai')
else:
    print('Nekeliamieji metai')
