# Užduotis 1 (pagal 6 paskaitos 1 užduotį)
# 6 paskaitos 1 užduotis – veiksmai su sakiniu
# Perdaryti 6-1 užduotį taip, kad:
# • Leistų vartotojui įvesti norimą sakinį
# • Sakinio objektui priskyrus įvestą sakinį iš vieno žodžio, parodytų
# pranešimą, kad sakinys turi būti bent iš dviejų žodžių
# • Paleistų visus klasės metodus

import sys

class Sentence:
    def __init__(self, sentence):
        self._sentence = sentence

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        self._sentence = sentence
        if len(sentence.split()) == 1:
            print("sakinys turi būti bent iš dviejų žodžių")
            sys.exit()

    @sentence.deleter
    def sentence(self):
        self._sentence = None

    def first_word(self):
        """ Gražintų pirmą sakinio žodį
        """
        return self._sentence.split()[0]

    def last_word(self):
        """Gražintų paskutinį sakinio žodį
        """
        return self._sentence.split()[-1]

    def reverse(self):
        """Gražintų sakinį atbulai
        """
        return self._sentence[::-1]

    def reverse_by_words(self):
        """Gražintų sakinį nuo paskutinio žodžio iki pirmojo
        """
        return self._sentence.split()[::-1]

    def capitalize(self):
        """Gražintų visas sakinio raides didžiosiomis
        """
        return tuple(st.capitalize() for st in self._sentence.split())

    def lowercase(self):
        """Gražintų visas sakinio raides mažosiomis
        """
        return tuple(st.lower() for st in self._sentence.split())

    def print_nums(self):
        """
        Atspausdintų, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

        Returns:
            tuple of ints: words in _sentence, numbers in _sentence, uppercase, lowercase
        """
        words = sum(word.isalpha() for word in self._sentence.split())
        nums = sum(word.isdigit() for word in self._sentence.split())
        uppercase = sum(letter.isupper() for letter in self._sentence)
        lowercase = sum(letter.islower() for letter in self._sentence)
        return words, nums, uppercase, lowercase

sakinys = Sentence("Microsoft cares about your privacy")
# sakinys.sentence = "Cia yra naujas sakinys"
sakinys.sentence = "Vienas du"

print(sakinys.first_word())
print(sakinys.last_word())
# print(sakinys.reverse())
# print(sakinys.reverse_by_words())
# print(sakinys.capitalize())
# print(sakinys.lowercase())
# print(sakinys.print_nums())
