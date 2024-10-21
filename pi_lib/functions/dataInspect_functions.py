# Funkcja sprawdzająca czy dane wejściowe są większe od 0
def isPositive(value):
    return 1 if value > 0 else 0

# Funkcja sprawdzająca czy dane wejściowe są mniejsze od 0
def isNegative(value):
    return 1 if value < 0 else 0

# Funkcja sprawdzająca czy dane wejściowe mogą zostać Float'em
def canBeFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Funkcja sprawdzająca czy dane wejściowe mogą zostać Int'em
def canBeInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False