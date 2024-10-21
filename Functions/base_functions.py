# Funkcja odpowiadająca za wyświetlanie error'ów
def errorMsg(text = "BŁĘDNY TYP DANYCH"):
    print("\n\033[1mBłąd: "+ text +"!\033[0m\n")

# Funkcja Sprawdzająca czy użytkownik chce zakończyć obliczenia
def close():
    a = input("Czy chcesz zakońcyć? ")
    if a.lower == "tak":
        return 1
    elif a.lower == "nie":
        return 0
    else:
        errorMsg
        return close