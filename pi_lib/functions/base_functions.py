from .dataInspect_functions import canBeInt, canBeFloat, canBeBool
# Funkcja odpowiadająca za wyświetlanie error'ów
def errorMsg(text = "BŁĘDNY TYP DANYCH"): print("\n\033[1mBłąd: "+ text +"!\033[0m\n")

# Funkcja Sprawdzająca czy użytkownik chce zakończyć obliczenia
def close():
    data = input("Czy chcesz zakońcyć? ")
    data = True if data in ["tak", "t", "yes", "y", "1", "true"] else False if data in ["nie", "n", "no", "0", "false", "f"] else '_'
    if type(data) == bool: return data
    errorMsg()
    return close()

# Funkcja wyświetlająca opisy działania funkcji i klas
def help(parameter = "all"):
    dictonary = {
        'errorMsg'      : '\033[1merrrorMsg(text)\033[0m -> Wyświetla komunikat o błędzie\ntext -> Nazwa błędu - default "BŁĘDNY TYP DANYCH"\n',
        'close'         : '\033[1mclose()\033[0m -> Pyta użytkownika czy chce zakończyć jeśli tak zwraca 1, a jak nie to 0\n',
        'gatData'       : '\033[1mgatData(text, type, sgn)\033[0m -> get and transform data -> pobiera od użytkownika dane i zmienia je na podany typ\ntext -> tekst wyświetlany użytkownikowi - default "Podaj liczbę: "\ntype -> typ na jaki ma być zamienione dane od użytkownika - default "i" - możliwe "i" int, "f" float\n',
        'isPositive'    : '\033[1misPositive(value)\033[0m -> Sprawdza czy wartość jest większa niż zero\nvalue -> wartość sprawdzana\n',
        'isNegative'    : '\033[1misNegative(value)\033[0m -> Sprawdza czy wartość jest mnejsza niż zero\nvalue -> wartość sprawdzana\n',
        'canBeFloat'    : '\033[1mcanBeFloat(value)\033[0m -> Sprawdza czy wartość może zostać Float\nvalue -> wartość sprawdzana\n',
        'canBeInt'      : '\033[1mcanBeFloat(value)\033[0m -> Sprawdza czy wartość może zostać Int\nvalue -> wartość sprawdzana\n',
        'classFigures'  : '\033[1mDostępne klasy figur:\033[0m\n1.Sphere -> radius, density\n2.Tetrahedron -> edge, density\n3.Pyramid -> edgeA, EdgeB, height, density\n4.Cylinder -> radius, height\n5.Cone -> radius, height, density\n6.Ellipsoid -> firstRadius, secondRadius, density\n\n\033[1mMetody klas figur które wyliczają:\033[0m\n1.calcSurfaceArea - wyliczanie pola powierzchni całkowitej\n2.calcVolume - wyliczania objętości\n3.calcMass - wyliczania masy\n4.calcAll - wszystkie powyższe i zwraca je jako słownik\n',
        'PlotClass'     : '\033[1mPlotClass()\033[0m -> Clasa do tworzenia Wykresów\n\n\033[1mMetody:\033[0m\n...\n'
        }
    if parameter in dictonary: print(dictonary[parameter])
    elif parameter == "all":
        for i in dictonary: print(dictonary[i])
    elif parameter == "classes":
        for i in dictonary:
            if i.startswith("class") or i.isupper(): print(dictonary[i])
    elif parameter == "functions":
        for i in dictonary:
            if i.islower() and not i.startswith("class"): print(dictonary[i])
    else: errorMsg("BŁĘDNY PARAMETR")

def loadFile(file_name): 
    with open(file_name, "r") as file: return file.read()

def inputData(text, outputType = "int"):
    if outputType not in [int, float, bool, string]:
        errorMsg("BŁĘDNY TYP!")
        return
    while True:
        value = input(text)
        if value == "-": break
        if outputType == "float" and canBeFloat(value): return float(value)
        if outputType == "int" and canBeInt(value): return int(value)
        if outputType == "bool" and canBeBool(value): return bool(value)
        if outputType == "string": return value
        errorMsg("BŁĘDNE DANE!")