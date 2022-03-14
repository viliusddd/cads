# Sukurti programą, kuri:
# • Prie kiekvieno sakinio „The Zen of Python tekstu“ žodžio pridėtų
# šauktuką ir atspausdintų naują sakinį.
# Patarimai:
# • Naudoti map (su lambda) arba comprehension, " ".join()

from functools import reduce

sakinys = 'The Zen of Python'

# print(' '.join([word + '!' for word in sakinys.split()]))

print(
    reduce(
        lambda x, y: x + ' ' + y,
        map(lambda x: x + '!', sakinys.split())
    )
)
