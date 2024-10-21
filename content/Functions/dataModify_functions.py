from base_functions import errorMsg
from dataInspect_functions import isPositive, isNegative, canBeFloat, canBeInt

# Funkcja pobierająca dane od użytkownika i zamieniająca typ danych na podany w funkcji
def gatData(text = "Podaj liczbę: ", type = 'i', sgn = 0): # gatData -> get and transform data
    while True:
        value = input(text)
        dictonary = {'i': canBeInt(value), 'f' : canBeFloat(value)}
        if dictonary[type.lower]:
            conditionSgn = isNegative(value) if sgn < 0 else isPositive(value) if sgn > 0 else True
            if conditionSgn:
                return int(value) if type.lower == "i" else float(value)
            else:
                errorMsg
        else:
            errorMsg