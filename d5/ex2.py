# Parašyti programą, kuri:
# • Leistų vartotojui įvesti sumą, išleistą restorane
# • Turėtų funkciją, kuri prie sumos pridėtų mokesčius (21 proc. PVM)
# • Turėtų funkciją, kuri prie sumos su PVM pridėtų arbatpinigius (15
# proc.)
# Programa turėtų pridėti prie įvestos sumos mokesčius, arbatpinigius
# (panaudojant funkcijas) ir atspausdinti bendrą sumą

entered_money = float(input("Enter the amount spent: "))

def sum_for_restaurant(money_sum, pvm=True, tips=True):
    pvm = money_sum * 0.25
    tips = (money_sum + pvm) * 0.15
    return money_sum + pvm + tips

print(sum_for_restaurant(entered_money))
