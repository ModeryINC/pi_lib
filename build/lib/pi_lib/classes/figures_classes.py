import numpy as np # type: ignore

class _Block():
    _pi = np.pi
    def calcMass(self): return round(self.density * self.calcVolume(), 2)
    def calcAll(self): return {'surfaceArea' : self.calcSurfaceArea(), 'volume' : self.calcVolume(), 'mass' : self.calcMass()}

class Sphere(_Block):
    def __init__(self, radius, density):
        self.radius = radius
        self.density = density
    def calcSurfaceArea(self): return round(4 * super()._pi * (self.radius) ** 2, 2)
    def calcVolume(self): return round((4 / 3) * super()._pi * self.radius ** 3, 2)

class Tetrahedron(_Block):
    def __init__(self, edge, density):
        self.edge = edge
        self.density = density
    def calcSurfaceArea(self): return round((self.edge ** 2) * (3 ** (1 / 2)), 2)
    def calcVolume(self): return round(((self.edge ** 3) * (2 ** (1 / 2))) / 12, 2)

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
    def calcVolume(self): return round((self.edgeA * self.edgeB * self.height) / 3, 2)

class Cylinder(_Block):
    def __init__(self, radius, height, density):
        self.radius = radius
        self.height = height
        self.density = density
        self._circleArea = round(super()._pi * (self.radius ** 2), 2)
        self._circleCircuit = round(2 * super()._pi * self.radius, 2)
    def calcSurfaceArea(self): return round((2 * self._circleArea) + (self.height * self._circleCircuit), 2)
    def calcVolume(self): return round(self._circleArea * self.height, 2)

class Cone(_Block):
    def __init__(self, radius, height, density):
        self.radius = radius
        self.height = height
        self.density = density
        self._circleArea = round(super()._pi * (self.radius ** 2), 2)
        self._lateral = round(((self.radius) ** 2 + self.height ** 2) ** (1 / 2), 2)
    def calcSurfaceArea(self): return round(super()._pi * self.radius * (self.radius * self._lateral), 2)
    def calcVolume(self): return round((self._circleArea * self.height) / 3, 2)

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
    def calcSurfaceArea(self): return round((2 * super()._pi * self.shortRadius) * (self.shortRadius + (self.longRadius / self._epsilon) * (np.arcsin(self._epsilon))), 2)
    def calcVolume(self): return round((4 * super()._pi * (self.shortRadius ** 2) * self.longRadius) / 3, 2)