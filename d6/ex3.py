# Sukurti programą, kuri:
# • Turėtų klasę Automobilis
# • Automobilis turėtų savybes: metai, modelis, kuro_tipas
# • Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie
# atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# • Sukūrus objektą, automatiškai atspausdintų automobilio metus,
# modelį ir kuro tipą
# • Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# • Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad
# jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_automonomiškai, kuris
# spausdintų „Važiuoja autonomiškai“
# • Sukurti norimą Automobilio objektą
# • Sukurti norimą Elektromobilio objektą
# • Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti,
# pildyti_degalu
# • Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti,
# pildyti_degalu, vaziuoti_automonomiškai

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self._print_specs()

    def _print_specs(self):
        print(f"Metai {self.metai}, modelis {self.modelis}, kuro tipas {self.kuro_tipas}")
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

print(auto.vaziuoti())
print(auto.stoveti())
print(auto.pildyti_degalu())
print()

elektro = Elektromobilis(2020, "Tesla", "elektra")

print(elektro.vaziuoti())
print(elektro.stoveti())
print(elektro.pildyti_degalu())
print(elektro.vaziuoti_automonomiskai())
