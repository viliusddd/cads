# Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius
# metus, nuo 1900 iki 2100 metų.

from calendar import isleap

for year in range(1900, 2101):
    if isleap(year):
        print(year)
