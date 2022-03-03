# Pagal 3 paskaitos 5 užduotį parašyti programą, kuri:
# • Leistų vartotojui įvesti metų rėžį (nuo...iki)
# • Turėtų funkciją, kuri įvestus metus priimtų kaip argumentus
# • Funkcija atspausdintų visus keliamuosius metus pagal duotus
# argumentus

from calendar import isleap

years_from = int(input("Insert years from: "))
years_to = int(input("Insert years to: "))

def year_range(from_year, to_year):
    for yr in range(from_year, to_year + 1):
        if isleap(yr):
            print(yr)

year_range(years_from, years_to)
