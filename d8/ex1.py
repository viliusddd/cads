# Sukurti programą, kuri:
# 1. Sukurtų failą „Tekstas.txt“ su „The Zen of Python tekstu“ tekstu.
# 2. Atspausdintų tekstą iš sukurto failo
# 3. Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# 4. Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į
# "Gražu yra geriau nei bjauru.":
# 6. Atspausdintų visą failo tekstą atbulai:
# 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir
# mažųjų raidžių:
# 8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik
# DIDŽIOSIOMIS RAIDĖMIS:
# Patarimai:
# • Naudoti from datetime import datetime, datetime.today()
# • Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# • Kai kur galima panaudoti funkcijas iš praeitų pamokų

from datetime import datetime, date

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 1. Sukurtų failą „Tekstas.txt“ su „The Zen of Python tekstu“ tekstu.
filename = 'Tekstas.txt'
with open(filename, 'w') as f:
    f.write(zen)

# 2. Atspausdintų tekstą iš sukurto failo
with open(filename) as f:
    print(f.read())

# 3. Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
with open(filename, 'a') as f:
    f.write(f'\n{datetime.now()}')

# 4. Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
new_text = ''
with open(filename, 'r+') as f:
    lines = f.readlines()
    new_lines = []

    for i in range(len(lines)):
        new_lines.append(f'{i + 1}. {lines[i]}')
    f.writelines(new_lines)

    for index, row in enumerate(f):
        new_text += f'{index} {row}'

# 5. Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į
# "Gražu yra geriau nei bjauru.":

filename = 'Tekstas.txt'

with open(filename, 'r+') as f:
    file = f.read()
    changed_file = file.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
    f.write(changed_file)

# 6. Atspausdintų visą failo tekstą atbulai:
with open(filename, 'r') as f:
    file = f.read()
    print(file[::-1])

# 7. Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir
# mažųjų raidžių:
with open(filename, 'r') as f:
    file = f.read()

    print(
        len(file.split()),
        sum(word.isdigit() for word in file.split()),
        sum(letter.isupper() for letter in file),
        sum(letter.islower() for letter in file),
    )

# 8. Nukopijuotų visą sukurto failą tekstą į naują failą, tik
# DIDŽIOSIOMIS RAIDĖMIS:
with open(filename, 'r+') as f:
    f.write(f.read().upper())
