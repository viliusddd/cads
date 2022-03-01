# Parašyti programą, kuri:
# • Atspausdintų dabartinę datą ir laiką
# • Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# • Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# • Atspausdintų dabartinę datą ir laiką tokiu formatu:
# 2019 03 08, 09:57.17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)
# https://www.w3schools.com/python/python_datetime.asp


from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Atspausdintų dabartinę datą ir laiką

subdays = datetime.today()
print((now + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"))  # Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų

print((now + timedelta(hours=8)).strftime("%Y %m %d, %H:%M.%S"))  # Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57.17
