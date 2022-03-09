
# Sukurti programą, kuri:
# • Leistų vartotojui įvesti norimą eilučių kiekį
# • Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# • Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Patarimai:
# • Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę
# (nuspaudus ENTER)

filename = 'file.txt'
new_filename = ''
text = ''

while True:
    user_input = input('Enter your text: ').strip()
    text += (user_input + '\n')

    if user_input == '':
        new_filename = input('Enter new filename: ')

        with open(new_filename, 'w') as f:
            f.write(text)
        break
