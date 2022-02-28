# Kauliukų žaidimas
# Sukurti programą, kuri:
# • Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# • Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# • Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import
# random), else, break

from random import sample

while True:
    nums = sample(range(1, 6), 3)
    print(f"Generated numbers: {nums}")
    if 5 in nums:
        print("Pralaimėjai...")
        break
    else:
        print("Laimėjai...")
        break
