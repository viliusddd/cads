# Pakeisti 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus
# klaidoms, programos mestų norimas klaidas lietuvių kalba (panaudoti
# try/except)

from datetime import datetime, date, timedelta

inp = None
date_obj = None
date_format = "%Y-%m-%d %H:%M"

try:
    inp = str(input("Enter date(yyy-mm-dd hh:mm): "))  # ex, 1989-08-11 12:04
    date_obj = datetime.strptime(inp, date_format)

    now = datetime.now()

    print(f"Praėjo {(time.days) // 365} metų")
    print(f"Praėjo {int(time.days * 0.0329)} mėnesių")
    print(f"Praėjo {int(time.days)} dienų")
    print(f"Praėjo {int(time.total_seconds()) // 3600} valandų")
    print(f"Praėjo {int(time.total_seconds()) // 60} minučių")
    print(f"Praėjo {int(time.total_seconds())} sekundžių")
except ValueError as exc:
    print(f'laiko duomenys \'{inp}\' neatitinka formato {date_format}')
except Exception:
    print("Įvyko neužgaudytas exceptionas")
