# Sukurti programą, kuri:
# • leistų vartotojui įvesti 5 žodžius
# • Pridėtų įvestus žodžius į sąrašą
# • Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą skaičių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

words = []

num = int(input('Insert number of words you\'d like to insert: '))

for i in range(num):
    inp = str(input(f'Insert {i+1} word: '))
    words.append(inp)

print(words)
for word in words:
    print(f'{word}: length is {len(word)}, it\'s position in list is {words.index(word)}')
