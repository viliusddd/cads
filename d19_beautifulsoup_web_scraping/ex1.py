# 1. Parašykite programą, kuri nuskaitytų Delfi antraštes, patikrintų, ar jos turi dvitaškį.
# Dalį iki dvitaškio sudėtų į vieną sąrašą, dalį po dvitaškio į kitą. Antrą sąrašą išmaišykite
# (Google). Tuomet atspausdinkite pirmas dalis iš pirmo sąrašo, prie jų prijunkite antras dalis iš
# antro sąrašo. Turėtume gauti panašių variantų:
# · Orai : už 9 šlakius teks sumokėti 26 tūkstančius eurų
# · Antradienio vakare kauniečius išgąsdino termofikacines elektrinė : ar bus naujagimių bumas?
# Sukurkite blogų žodžių sąrašą, pagal kurį išsifiltruoja pranešimai apie COVID, mirtis ir t.t.
# Išfiltruokite ankstyvoje stadijoje, kol dar antraštės neperskirtos.

import random
import requests

from bs4 import BeautifulSoup


response = requests.get('https://delfi.lt').text
soup = BeautifulSoup(response, 'html.parser')

before_colon, after_colon = [], []

for title in soup.find_all('a', class_='CBarticleTitle'):
    try:
        title = title.text
        if ':' in title:
            if not any(i in title for i in ['COVID', 'mirtis']):
                split_title = title.split(':')

                before_colon.append(split_title[0])
                after_colon.append(split_title[1])
    except:
        pass

random.shuffle(after_colon)

for num, before in enumerate(before_colon):
        print(f'{before}:{after_colon[num]}')
