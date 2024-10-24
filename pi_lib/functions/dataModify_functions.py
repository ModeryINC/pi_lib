from .base_functions import errorMsg
from .dataInspect_functions import isPositive, isNegative, canBeFloat, canBeInt

# Funkcja pobierająca dane od użytkownika i zamieniająca typ danych na podany w funkcji
def gatData(text = "Podaj liczbę: ", type = "i", sgn = 0): # gatData -> get and transform data
    while True:
        value = input(text)
        dictonary = {"i": canBeInt(value), "f" : canBeFloat(value)}
        try:
            dictonary[type]
            if dictonary[type]:
                conditionSgn = isNegative(float(value)) if sgn < 0 else isPositive(float(value)) if sgn > 0 else True
                if conditionSgn:
                    return int(value) if type.lower == "i" else float(value)
                else:
                    errorMsg()
            else:
                errorMsg()
        except KeyError:
            errorMsg("BŁĘDNY PARAMETR type")

def removeWhitespaces(value):
    try:
        value.replace(" ", "")
        value = value.replace(" ", "")
        value = value.replace("'", "")
        value = value.replace(",", ".")
        value = value.replace("%", "")
        return value
    except:
        return False