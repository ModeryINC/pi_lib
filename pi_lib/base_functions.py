# Funkcja odpowiadająca za wyświetlanie error'ów
def errorMsg(text = "BŁĘDNY TYP DANYCH"):
    print("\n\033[1mBłąd: "+ text +"!\033[0m\n")

# Funkcja Sprawdzająca czy użytkownik chce zakończyć obliczenia
def close():
    a = input("Czy chcesz zakońcyć?")
    if a.lower == "tak":
        return 1
    elif a.lower == "nie":
        return 0
    else:
        errorMsg
        return close
    
def help(parameter = "all"):
    dictonary = {
        'errorMsg'      : '\033[1merrrorMsg(text)\033[0m -> Wyświetla komunikat o błędzie\ntext -> Nazwa błędu - default "BŁĘDNY TYP DANYCH"\n',
        'close'         : '\033[1mclose()\033[0m -> Pyta użytkownika czy chce zakończyć jeśli tak zwraca 1, a jak nie to 0\n',
        'gatData'       : '\033[1mgatData(text, type, sgn)\033[0m -> get and transform data -> pobiera od użytkownika dane i zmienia je na podany typ\ntext -> tekst wyświetlany użytkownikowi - default "Podaj liczbę: "\ntype -> typ na jaki ma być zamienione dane od użytkownika - default "i" - możliwe "i" int, "f" float\n',
        'classFigures'  : '\033[1mKlasy które pobierają odpowiednie dane do wyliczenia:\033[0m\n1.calcSurfaceArea - wyliczanie pola powierzchni całkowitej\n2.calcVolume - wyliczania objętości\n3.calcMass - wyliczania masy\n4.calcAll - wszystkie powyższe i zwraca je jako słownik\n'
        }
    if parameter in dictonary:
        print(dictonary[parameter])
    elif parameter == "all":
        for i in dictonary:
            print(dictonary[i])
    else:
        errorMsg("BŁĘDNY PARAMETR")