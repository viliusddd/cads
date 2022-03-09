# Parašyti funkciją, kuri patikrintų ar duotas stringas yra palindromas ar ne.
# Palindromas - žodis, žodžių grupė, sakinys, posakis a eilėraštis, kuris
# skaitomas iš galo, reiškia tą patį arba bent yra prasmingas.

def is_palindrome(sentence: str):
    return sentence.lower() == sentence[::-1].lower()

print(is_palindrome("vieeiv"))
