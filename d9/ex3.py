# Duotas sąrašas:
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Sukurti programą, kuri:
# • Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# • Sudėtų ir atspausdintų visus sąrašo žodžius
# • Suskaičiuotų ir atspausdintų, kiek sąrašę yra loginių (boolean)
# kintamųjų su True reikšme
# Patarimai:
# • Naudoti filter arba comprehension, sum, " ".join()

from functools import reduce

# • Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# print(sum([i for i in sarasas if type(i) in (float, int)]))
print(
    reduce(
        lambda x, y: x+y,
        list(filter(lambda x: type(x) in (float, int), sarasas))
    )
)

# • Sudėtų ir atspausdintų visus sąrašo žodžius
# print(''.join([i for i in sarasas if type(i) is str]))
print(
    reduce(
        lambda x, y: x+y,
        list(filter(lambda x: type(x) is str, sarasas))
    )
)

# • Suskaičiuotų ir atspausdintų, kiek sąrašę yra loginių (boolean)
# print(sum([item for item in sarasas if (type(item) is bool) and (item == True)]))
print(
    reduce(
        lambda x, y: x + y,
        list(filter(lambda x: (type(x) is bool) and (x == True), sarasas))
    )
)
