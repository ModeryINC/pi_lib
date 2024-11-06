from ..functions.dataInspect_functions import canBeFloat, canBeInt
from ..functions.plot_functions import createPlot
from scipy.io.wavfile import write # type: ignore
import numpy as np # type: ignore

class PlotClass():
    amplitude = .1
    frequency = 440
    rate = 44100
    time = 5
    data = []
    
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
    
    # Metody tworzące
    def createWav(self, data, fileName):
        audioData = np.int16(data * (2 ** 15))
        write(f'./PI_Cwiczenia31_10_24/{fileName}.wav', self.rate, audioData)
    
    def drawPlot(self, viewStart = 0, viewEnd = .01, index = -1): createPlot(y=self.data[index], viewStart=viewStart, viewEnd=viewEnd, lenght=self.time, rate=self.rate)
    
    # Metody usuwające
    def dropData(self, id = -1): self.data.pop(id)
    
    # Metody generujące
    def sin(self):      self.data.append(self.amplitude * np.sin(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate)))
    def sgnSin(self):   self.data.append(self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * np.linspace(0, self.time, self.time * self.rate))))
    def whiteNoise(self):
        linespace = np.linspace(0, self.time, self.time * self.rate)
        randomValuesLinespace = linespace + np.random.uniform(-1, 1, size=linespace.size)
        self.data.append(self.amplitude * 2 * self.frequency * randomValuesLinespace)
    def sawtooth(self): pass
    def triangle(self): pass
    
    def fourierTransform(self, id = -1):
        length = len(self.data[id])
        deltaTime = self.data[id][1] - self.data[id][0]
        list = []
        for i in range(length):
            sum = 0
            for j in range(length): sum += self.data[id][j] * np.exp(-2 * j * np.pi * i * (j / length))
            list.append(sum)
        x = np.array([i * (self.frequency / length) for i in range(length)])
        y = np.abs(np.array(list))
        createPlot( x = x[:length // 2],y = y[: length // 2], viewEnd = max(self.data[id]))