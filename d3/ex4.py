# Kauliukų žaidimas
# Sukurti programą, kuri:
# • Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# • Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# • Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import
# random), else, break

from random import randint

first = randint(1, 6)
second = randint(1, 6)
third = randint(1, 6)

nums = first, second, third

print(nums)

for num in nums:
    if num == 5:
        print("Pralaimėjai...")
        break
