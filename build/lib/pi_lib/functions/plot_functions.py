from scipy.io.wavfile import read # type: ignore
import numpy as np # type: ignore
from matplotlib.pyplot import plot, show, xlim # type: ignore

# Funkcja zwracająca długość pliku .wav w sekundach
def getWavLength(rate, data): return len(data) / rate

# Funkcja odczytująca plik .wav
def readWav(path): return read(path)

# Funkcja rysująca wykres
def createPlot(x = 1, y = 1, viewStart = 0, viewEnd = .01, lenght = 5, rate = 1, start = 0):
    if not (isinstance(y,'np.ndarray') or isinstance(y, list)):
        y = []
        for i in range[0, lenght * rate]:
            y.append(np.random.uniform(-1, 1))
    if not (isinstance(x,'np.ndarray') or isinstance(x, list)):
        x = np.linspace(start, lenght, lenght * rate)
    plot(x, y)
    xlim(viewStart, viewEnd)
    show()

# Funkcja rysująca wykres z pliu .wav
def createPlotFromWav(wavFile, viewStart = 0, viewEnd = .01):
    rate, y = wavFile
    wavFileLength = getWavLength(rate, y)
    x = np.linspace(0, int(wavFileLength), int(wavFileLength * rate))
    createPlot(x, y, viewStart, viewEnd)