# Parašyti funkciją, kuriai perduodami du kintamieji a ir b.
# • Kintamasis a yra sveikųjų skaičių sąrašas, kintamasis b yra sveikasis skaičius.
# • Kintamajame a raskite pirmą dviejų skaičių porą, kurios suma yra lygi kintamajam b.
# • Jeigu tokios poros nėra, praneškite.

def sum_of_list_items_to_comp(a: list, b: int):

    for i, this in enumerate(a):
        for that in a[i+1:]:
            if this + that == b:
                return [this, that]
            else:
                return "Nothing was found"

print(sum_of_list_items_to_comp([1,2,3], 5))