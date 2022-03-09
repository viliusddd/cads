# Užduotis 2 (pagal 3 paskaitos 3 užduotį)
# Sukurti klasę, kuri turėtų savybę sukaktis ir metodus, kurie gražintų,
# kiek nuo įvestos sukakties praėjo:
# 1. Metų
# 2. Mėnesių
# 3. Savaičių
# 4. Dienų
# 5. Valandų
# 6. Minučių
# 7. Sekundžių
# Sukurti objektą (-us) ir išbandyti visus sukurtos klasės metodus

from datetime import datetime


class Anniversary():

    now = datetime.now()

    def __init__(self, anniversary):
        self.anniversary = datetime.strptime(anniversary, "%Y-%m-%d")
        self.passed = self.now - self.anniversary

    def years(self):
        return f"Praėjo {(self.passed.days) // 365} metų"

    def months(self):
        return f"Praėjo {int(self.passed.days * 0.0329)} mėnesių"

    def weeks(self):
        return f"Praėjo {self.passed.days // 7} savaičių"

    def days(self):
        return f"Praėjo {self.passed.days} dienų"

    def hours(self):
        return f"Praėjo {int(self.passed.total_seconds()) // 3600} valandų"

    def minutes(self):
        return f"Praėjo {int(self.passed.total_seconds()) // 60} minučių"

    def seconds(self):
        return f"Praėjo {int(self.passed.total_seconds())} sekundžių"

ann = Anniversary('1989-01-11')

print(ann.years())
print(ann.months())
print(ann.weeks())
print(ann.days())
print(ann.hours())
print(ann.seconds())
