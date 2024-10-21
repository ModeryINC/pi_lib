import numpy as np

class _Block():
    _pi = np.pi
    
    def calcMass(self):
        try:
            self.volume
            condition = 0
        except:
            condition = 1
        if condition:
            self.calcVolume()
        self.mass = round(self.density * self.volume, 2)
        return self.mass
    
    def calcAll(self):
        self.calcSurfaceArea(), self.calcVolume(), self.calcMass()
        return {'surfaceArea' : self.surfaceArea, 'volume' : self.volume, 'mass' : self.mass}


class Sphere(_Block):
    def __init__(self, radius, density):
        self.radius = radius
        self.density = density
    
    def calcSurfaceArea(self):
        self.surfaceArea = round(4 * super()._pi * (self.radius) ** 2, 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round((4 / 3) * super()._pi * self.radius ** 3, 2)
        return self.volume

class Tetrahedron(_Block):
    def __init__(self, edge, density):
        self.edge = edge
        self.density = density
    
    def calcSurfaceArea(self):
        self.surfaceArea = round((self.edge ** 2) * (3 ** (1 / 2)), 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round(((self.edge ** 3) * (2 ** (1 / 2))) / 12, 2)
        return self.volume
    
class Pyramid(_Block):
    def __init__(self, edgeA, edgeB, height, density):
        self.edgeA = edgeA
        self.edgeB = edgeB
        self.height = height
        self.density = density
        
        self._triangleHeightA = round(((self.edgeB / 2) ** 2 + self.height ** 2) ** (1 / 2), 2)
        self._triangleHeightB = round(((self.edgeA / 2) ** 2 + self.height ** 2) ** (1 / 2), 2)
    
    def calcSurfaceArea(self):
        self._triangleAreaA = (self.edgeA * self._triangleHeightA) / 2
        self._triangleAreaB = (self.edgeB * self._triangleHeightB) / 2
        self.surfaceArea = round(self.edgeA * self.edgeB + 2 * (self._triangleAreaA + self._triangleAreaB), 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round((self.edgeA * self.edgeB * self.height) / 3, 2)
        return self.volume

class Cylinder(_Block):
    def __init__(self, radius, height, density):
        self.radius = radius
        self.height = height
        self.density = density
        
        self._circleArea = round(super()._pi * (self.radius ** 2), 2)
        self._circleCircuit = round(2 * super()._pi * self.radius, 2)
    
    def calcSurfaceArea(self):
        self.surfaceArea = round((2 * self._circleArea) + (self.height * self._circleCircuit), 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round(self._circleArea * self.height, 2)
        return self.volume

class Cone(_Block):
    def __init__(self, radius, height, density):
        self.radius = radius
        self.height = height
        self.density = density
        
        self._circleArea = round(super()._pi * (self.radius ** 2), 2)
        self._lateral = round(((self.radius) ** 2 + self.height ** 2) ** (1 / 2), 2)
    
    def calcSurfaceArea(self):
        self.surfaceArea = round(super()._pi * self.radius * (self.radius * self._lateral), 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round((self._circleArea * self.height) / 3, 2)
        return self.volume

class Ellipsoid(_Block):
    def __init__(self, firstRadius, secondRadius, density):
        self.density = density
        
        if firstRadius <= secondRadius:
            self.shortRadius = firstRadius
            self.longRadius = secondRadius
        elif firstRadius > secondRadius:
            self.longRadius = firstRadius
            self.shortRadius = secondRadius
        
        self._epsilon = round((1 - ((self.shortRadius ** 2) / (self.longRadius ** 2))) ** (1 / 2), 2)
    
    def calcSurfaceArea(self):
        self.surfaceArea = round((2 * super()._pi * self.shortRadius) * (self.shortRadius + (self.longRadius / self._epsilon) * (np.arcsin(self._epsilon))), 2)
        return self.surfaceArea
    
    def calcVolume(self):
        self.volume = round((4 * super()._pi * (self.shortRadius ** 2) * self.longRadius) / 3, 2)
        return self.volume