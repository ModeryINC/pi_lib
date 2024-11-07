from scipy.io.wavfile import read # type: ignore
import numpy as np # type: ignore
from matplotlib.pyplot import plot, show, xlim # type: ignore

# Funkcja zwracająca długość pliku .wav w sekundach
def getWavLength(rate, data): return len(data) / rate

# Funkcja odczytująca plik .wav
def readWav(path): return read(path)

# Funkcja rysująca wykres
def createPlot(x = [], y = [], viewStart = 0, viewEnd = .01, lenght = 5, rate = 1, start = 0):
    # if np.array_equal(y, []): y = np.sin(2 * np.pi * 0.8 * np.linspace(start, lenght, lenght * rate))
    if np.array_equal(x, []): x = np.linspace(start, int(len(y) / rate), int(len(y)))
    y[0] = start
    print(x)
    print(y)
    plot(x, y)
    xlim(viewStart, viewEnd)
    show()

# Funkcja rysująca wykres z pliu .wav
def createPlotFromWav(wavFile, viewStart = 0, viewEnd = .01):
    rate, y = wavFile
    wavFileLength = getWavLength(rate, y)
    x = np.linspace(0, int(wavFileLength), int(wavFileLength * rate))
    createPlot(x, y, viewStart, viewEnd)