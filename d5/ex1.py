# Sukurti ir paleisti funkcijas, kurios:
# • Sudėtų ir atspausdintų visus paduotus skaičius
# • Atspausdintų didžiausią iš kelių paduotų skaičių
# • Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
# • Patikrintų ir atspausdintų, ar paduotas skaičius yra paduotame sąraše
# • Atspausdintų, kiek paduotame stringe yra žodžių, skaičių, didžiųjų ir
# mažųjų raidžių
# • Atspausdintų visus paduoto rėžio (nuo… iki) lyginius skaičius

def print_sum_of_nums(*args):
    """
    Sudeda ir atspausdina visus paduotus skaičius
    """
    print(sum(args))

def print_highest_num(*args):
    """
    Atspausdina didžiausią iš kelių paduotų skaičių
    """
    print(max(args))

def align_backwards(words: str):
    """
    Išrikiuoja paduoto stringo žodžius nuo paskutinio iki pirmojo

    Args:
        words (str): multiple words separated by space

    Returns:
        str: returns original input but reversed
    """
    return " ".join(words.split()[::-1])

def print_if_num_in_list(num, num_list):
    """
    Patikrintų ir atspausdintų, ar paduotas skaičius yra paduotame sąraše

    Args:
        num (int): number
        num_list (list): list of numbers
    """
    print(num in num_list)

def print_word_info(sentence):
    """
    Atspausdinta kiek paduotame stringe yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

    Args:
        sentence (str): string
    """
    split_sentence = sentence.split()

    words = sum(word.isalpha() for word in split_sentence)
    nums = sum(word.isdigit() for word in split_sentence)
    uppercase = sum(letter.isupper() for letter in sentence)
    lowercase = sum(letter.islower() for letter in sentence)

    print(words)
    print(nums)
    print(uppercase)
    print(lowercase)
    print('')

def equal_nums(nuo, iki):
    """
    Atspausdina visus paduoto rėžio (nuo… iki) lyginius skaičius

    Args:
        nuo (int): pirmas skaičius
        iki (int): antras skaičius
    """
    for i in range(nuo, iki + 1):
        if i % 2:
            print(i)

print_sum_of_nums(1,2,3)
print_highest_num(1,2,3)
print(align_backwards("This is sentence"))
print_if_num_in_list(2, [1, 2, 3])
print_word_info("This is another sentence with 1 number")
equal_nums(1, 6)
