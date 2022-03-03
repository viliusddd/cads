# Parašyti funkciją, kuri du duotus skaičius padalina tarpusavyje ir atspausdina rezultatą
# Sąlygos:
# * jei antras parametras paduotas yra 0, tuomet atspausdinam "Division by zero not allowed"
# * jei bent vienas parametras yra ne skaičius, tuomet atspausdinam "Both parameters have to be
#   numbers" ir iššaukiam exceptioną
# * visais atvejais, kai metodas baigiasi, atspausdinam "Execution finished"

def divide_number(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        return "Division by zero not allowed"
    except TypeError:
        return "Both parameters have to be numbers"
    finally:
        return "Execution finished"

print(divide_number(6, 2))
