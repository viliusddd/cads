# Pakeisti 1 užduotis taip, kad neteisingai įvedus duomenis ar įvykus
# klaidoms, programos mestų norimas klaidas lietuvių kalba (panaudoti
# try/except)

try:
    inp = int(input("Input number: "))
    if inp <= 0:
        print(False)
    else:
        print(True)
except ValueError as exc:
    print(f'netinkamas int() literatas su 10 baze: {exc.args[-1].split(": ")[-1]}')
except Exception:
    print("Įvyko neužgaudytas exceptionas")
