# Parašyti funkciją, kuri du duotus skaičius padalina tarpusavyje ir atspausdina rezultatą
# Sąlygos:
# * jei antras parametras paduotas yra 0, tuomet atspausdinam "Division by zero not allowed"
# * jei bent vienas parametras yra ne skaičius, tuomet atspausdinam "Both parameters have to be
#   numbers" ir iššaukiam exceptioną
# * visais atvejais, kai metodas baigiasi, atspausdinam "Execution finished"

def divide_numbers(first, second):
    try:
        print(first / second)
    except ZeroDivisionError:
        print("Division by zero not allowed")
        raise
    except TypeError:
        print("Both parameters have to be numbers")
        raise
    finally:
        print("Execution finished")

divide_numbers(6, 3)
divide_numbers(6, 0)
divide_numbers(6, "a")
