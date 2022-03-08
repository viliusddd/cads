# Užduotis 2 (pagal 6 paskaitos 2 užduotį)
# 6 paskaitos 2 užduotis – programa, skaičiuojanti, kiek metų, mėnesių,
# savaičių, dienų, valandų, minučių, sekundžių praėjo nuo įvestos datos
# Perdaryti 6-2 užduotį taip, kad:
# • Leistų vartotojui įvesti norimą datą
# • Parodytų pranešimą apie neteisingai įvestus metus, jei jie mažesni už
# 0 arba didesni už 3000
# • Parodytų pranešimą apie neteisingai įvestą mėnesį, jei jis mažesnis
# už 1 arba didesnis už 12
# • Parodytų pranešimą apie neteisingai įvestą dieną, jei ji mažesnė už 1
# arba didesnė už 31
# • Parodytų pranešimą apie neteisingai įvestą valandą, jei ji mažesnė už
# 0 arba didesnė už 24
# • Parodytų pranešimą apie neteisingai įvestas minutes, jei jos mažesnė
# už 1 arba didesnės už 60

import sys

from datetime import datetime


class Anniversary():

    now = datetime.now()

    def __init__(self, date):
        self._date = date
        self.passed = self.now - datetime.strptime(date, "%Y-%m-%d")

        self._years = self.passed.days // 365
        self._months = int(self.passed.days * 0.0329)
        self._days = self.passed.days
        self._hours = int(self.passed.total_seconds()) // 3600
        self._minutes = int(self.passed.total_seconds()) // 60


    @property
    def date(self):
        return self._date

    @date.deleter
    def date(self):
        del self.passed

    @date.setter
    def date(self, date):
        self._date = date
        self.passed = self.now - datetime.strptime(date, "%Y-%m-%d")
        self._years = self.passed.days // 365
        self._months = int(self.passed.days * 0.0329)
        self._days = self.passed.days
        self._hours = int(self.passed.total_seconds()) // 3600
        self._minutes = int(self.passed.total_seconds()) // 60

    def years(self):
        if 0 < int(self._years) < 3000:
            return f"Praėjo {self._years} metų"
        else:
            return f"Wrong years input: {self._years}"

    def months(self):
        if 1 < self._months < 12:
            return f"Praėjo {self._months} mėnesių"
        else:
            return f"Wrong months input: {self._months}"

    def days(self):
        if 1 < self._days < 31:
            return f"Praėjo {self._days} dienų"
        else:
            return f"Wrong months input: {self._days}"


    def hours(self):
        if 0 < self._hours < 24:
            return f"Praėjo {self._hours} valandų"
        else:
            return f"Wrong hours input: {self._hours}"

    def minutes(self):
        if 1 < self._minutes < 64:
            return f"Praėjo {self._minutes} minučių"
        else:
            return f"Wrong minutes input: {self._minutes}"

ann = Anniversary('1989-01-11')
ann.date = '4020-01-11'
print(ann.date)
print(ann.years())

print(ann.months())
print(ann.days())
print(ann.hours())
