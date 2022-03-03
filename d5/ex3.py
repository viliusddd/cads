# Pagal 3 paskaitos 5 užduotį parašyti programą, kuri:
# • Leistų vartotojui įvesti metų rėžį (nuo...iki)
# • Turėtų funkciją, kuri įvestus metus priimtų kaip argumentus
# • Funkcija atspausdintų visus keliamuosius metus pagal duotus
# argumentus

from calendar import isleap

def year_range(from_year, to_year):
    for yr in range(from_year, to_year):
        if isleap(yr):
            print('Keliamieji metai')
        else:
            print('Nekeliamieji metai')

year_range(1989, 2011)