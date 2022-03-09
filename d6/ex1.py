# Užduotis 1 (pagal 2 ir 5 paskaitos užduotis)
# Sukurti klasę, kuri turėtų savybę sakinys ir metodus, kurie:
# • Gražintų pirmą sakinio žodį
# • Gražintų paskutinį sakinio žodį
# • Gražintų sakinį atbulai
# • Gražintų sakinį nuo paskutinio žodžio iki pirmojo
# • Gražintų visas sakinio raides didžiosiomis
# • Gražintų visas sakinio raides mažosiomis
# • Atspausdintų, kiek sakinyje yra žodžių, skaičių, didžiųjų ir
# • mažųjų raidžių
# • Sukurti objektą (-us) ir išbandyti visus sukurtos klasės metodus

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def first_word(self):
        """ Gražintų pirmą sakinio žodį
        """
        return self.sentence.split()[0]

    def last_word(self):
        """Gražintų paskutinį sakinio žodį
        """
        return self.sentence.split()[-1]

    def reverse(self):
        """Gražintų sakinį atbulai
        """
        return self.sentence[::-1]

    def reverse_by_words(self):
        """Gražintų sakinį nuo paskutinio žodžio iki pirmojo
        """
        return self.sentence.split()[::-1]

    def capitalize(self):
        """Gražintų visas sakinio raides didžiosiomis
        """
        return tuple(st.capitalize() for st in self.sentence.split())

    def lowercase(self):
        """Gražintų visas sakinio raides mažosiomis
        """
        return tuple(st.lower() for st in self.sentence.split())

    def print_nums(self):
        """
        Atspausdintų, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

        Returns:
            tuple of ints: words in sentence, numbers in sentence, uppercase, lowercase
        """
        words = sum(word.isalpha() for word in self.sentence.split())
        nums = sum(word.isdigit() for word in self.sentence.split())
        uppercase = sum(letter.isupper() for letter in self.sentence)
        lowercase = sum(letter.islower() for letter in self.sentence)
        return words, nums, uppercase, lowercase

sentence = Sentence("Microsoft cares about your privacy")

print(sentence.first_word())
print(sentence.last_word())
print(sentence.reverse())
print(sentence.reverse_by_words())
print(sentence.capitalize())
print(sentence.lowercase())
print(sentence.print_nums())
