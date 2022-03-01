# Parašyti programą, kuri:
# • Leistų vartotojui įvesti sveiką skaičių.
# • Atspausdinti True, jei skaičius teigiamas
# • Atspausdinti False, jei skaičius neigiamas ar lygus 0
# • True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį
# ar_skaicius_teigiamas
# Patarimas: naudoti input, boolean, if/else

inp = int(input("Input number: "))
if inp <= 0:
    print(False)
else:
    print(True)
