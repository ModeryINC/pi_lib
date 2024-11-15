from ..functions.dataInspect_functions import canBeFloat, canBeInt
from ..functions.plot_functions import createPlot, createPlotPyqt
from scipy.io.wavfile import write # type: ignore
from scipy.signal import sawtooth # type: ignore
import numpy as np # type: ignore

class PlotClass():
    amplitude = .1
    frequency = 440
    rate = 44100
    time = 5
    data = [[(amplitude * np.sin(2 * np.pi * frequency * np.linspace(0, time, time * rate))), amplitude, frequency, rate, time]]
    
    def __init__(self): pass
    
    # settery
    def setAmplitude(self, value):
        if not canBeFloat(value): return
        if float(value) == 0: return
        self.amplitude = value
    
    def setFrequency(self, value):
        if not canBeInt(value): return
        if int(value) == 0: return
        self.frequency = value
    
    def setTime(self, value):
        if not canBeInt(value): return
        if int(value) == 0: return
        self.time = value
    
    def setRate(self, value):
        if not canBeInt(value): return
        if int(value) == 0: return
        self.rate = value
    
    # Metody tworzące
    def saveToWav(self, fileName = 'wavFile', id = -1):
        audioData = np.int16(self.data[-1][0] * (2 ** 15))
        write(f'./PI_Cwiczenia31_10_24/{fileName}.wav', self.data[id][3], audioData)
    
    def drawPlot(self, viewStart = 0, viewEnd = .01, id = -1): createPlot(y=self.data[id][0], viewStart=viewStart, viewEnd=viewEnd, rate=self.data[id][3])
    
    def saveToCsv(self, x = data[len(data) - 1][4], y = data[len(data) - 1][0], id = -1, fileName = "wykresCsv"):
        if np.array_equal(y, self.data[-1][0]) and id != -1: y = self.data[id][0]
        import pandas as pd  #type: ignore
        dataFrame = pd.DataFrame({'x': x, 'y': y})
        dataFrame.to_csv(f"./PI_Cwiczenia31_10_24/{fileName}.csv", index=True)
    
    # Metody usuwające
    def dropData(self, id = -1): self.data.pop(id)
    
    # Metody generujące
    def sin(self):self.data.append([self.amplitude * np.sin(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate)), self.amplitude, self.frequency, self.rate, self.time])
    
    def sgnSin(self): self.data.append([self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate))), self.amplitude, self.frequency, self.rate, self.time])
    
    def sawtooth(self): self.data.append([sawtooth(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate)), self.amplitude, self.frequency, self.rate, self.time])
    
    def triangle(self): self.data.append([sawtooth(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate), width=0.5), self.amplitude, self.frequency, self.rate, self.time])
    
    def whiteNoise(self):
        linespace = np.linspace(0, self.time, self.time * self.rate)
        randomValuesLinespace = linespace + np.random.uniform(-1, 1, size=linespace.size)
        self.data.append([self.amplitude * 2 * self.frequency * randomValuesLinespace, self.amplitude, self.frequency, self.rate, self.time])
    
    def fourierTransform(self, id = -1, save = 0, show = 1, fileName = "transformataFouriera"):
        length = len(self.data[id][0])
        fourierValues = np.fft.fft(self.data[id][0])
        x = np.fft.fftfreq(len(fourierValues), 1/self.data[id][3])
        y = np.abs(fourierValues)
        if save: self.saveToCsv(x = x[:length // 2], y = y[: length // 2], fileName = fileName)
        if show: createPlot(x = x[:length // 2], y = y[: length // 2], viewEnd = 3000)

class PlotClassPyqt(PlotClass):
    def drawPlot(self, graph = None, id = -1): createPlotPyqt(y=self.data[id][0], graph=graph, rate=self.data[id][3])
    def fourierTransform(self, id = -1, save = 0, show = 1, graph = None, fileName = "transformataFouriera"):
        length = len(self.data[id][0])
        fourierValues = np.fft.fft(self.data[id][0])
        x = np.fft.fftfreq(len(fourierValues), 1/self.data[id][3])
        y = np.abs(fourierValues)
        if save: self.saveToCsv(x = x[:length // 2], y = y[: length // 2], fileName = fileName)
        if show: createPlotPyqt(x = x[:length // 2], y = y[: length // 2], graph = graph)