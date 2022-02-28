# Parašyti programą, kuri:
# • Leistų vartotojui įvesti skaičių.
# • Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# • Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų
# įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, brake

nums = 0

while True:
    human_input = int(input("Please insert number: "))

    if human_input > 0:
        nums += human_input
    else:
        break

print(nums)
