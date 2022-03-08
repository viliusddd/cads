# Užduotis 3 (pagal 6 paskaitos 3 užduotį)
# 6 paskaitos 3 užduotis – sukurti automobilio objektą
# Perdaryti 6-3 užduotį taip, kad:
# • Leistų vartotojui įvesti automobilio modelį, metus ir kuro tipą
# • Parodytų pranešimą apie neteisingai įvestus metus, jei jie mažesni už
# 1800 arba didesni už 2200
# • Atspausdintų informaciją apie automobilį: įvestus metus, modelį bei
# kuro tipą

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self._metai = metai
        self._modelis = modelis
        self._kuro_tipas = kuro_tipas
        self._print_specs()

    def get_metai(self):
        return self._metai

    def set_metai(self, metai):
        self._metai = metai

    def del_metai(self):
        del self._metai

    metai = property(get_metai, set_metai, del_metai)

    def get_modelis(self):
        return self._modelis

    def set_modelis(self, modelis):
        self._modelis = modelis

    def del_modelis(self):
        del self._modelis

    modelis = property(get_modelis, set_modelis, del_modelis)

    def get_kuro_tipas(self):
        return self._kuro_tipas

    def set_kuro_tipas(self, kuro_tipas):
        self._kuro_tipas = kuro_tipas

    def del_kuro_tipas(self):
        del self._kuro_tipas

    kuro_tipas = property(get_kuro_tipas, set_kuro_tipas, del_kuro_tipas)

    def _print_specs(self):
        print(f"Metai {self._metai}, modelis {self._modelis}, kuro tipas {self._kuro_tipas}")
    def vaziuoti(self):
        return "Važiuoja"

    def stoveti(self):
        return "Priparkuota"

    def pildyti_degalu(self):
        return "Degalai įpilti"

class Elektromobilis(Automobilis):

    def pildyti_degalu(self):
        return "Baterija įkrauta"

    def vaziuoti_automonomiskai(self):
        return "Važiuoja autonomiškai"


auto = Automobilis(1988, "Audi", "benzinas")
auto.metai = 1975
auto.modelis = 'VW Golf'
auto.kuro_tipas = 'kerosene'

print(auto.vaziuoti())
print(auto.stoveti())
print(auto.pildyti_degalu())
auto._print_specs()

# elektro = Elektromobilis(2020, "Tesla", "elektra")

# print(elektro.vaziuoti())
# print(elektro.stoveti())
# print(elektro.pildyti_degalu())
# print(elektro.vaziuoti_automonomiskai())
