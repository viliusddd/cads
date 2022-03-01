# Parašyti programą, kuri:
# • Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# • Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# 1. Metų
# 2. Mėnesių
# 3. Dienų
# 4. Valandų
# 5. Minučių
# 6. Sekundžių
# Patarimas: naudoti datetime, .days, .total_seconds()

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

inp = str(input("Enter date(yyy-mm-dd hh:mm): "))  # ex, 1989-08-11 12:04
date_obj = datetime.strptime(inp, "%Y-%m-%d %H:%M")

now = datetime.now()
print(f"Now time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

time = now - date_obj

print(f"Praėjo {(time.days) // 365} metų")
print(f"Praėjo {int(time.days * 0.0329)} mėnesių")
print(f"Praėjo {int(time.days)} dienų")
print(f"Praėjo {int(time.total_seconds()) // 3600} valandų")
print(f"Praėjo {int(time.total_seconds()) // 60} minučių")
print(f"Praėjo {int(time.total_seconds())} sekundžių")
