import math
from itertools import izip
class Vector:
    exponentDict = {}
    unitVector = dict()
    
    def __init__(self, XVector, YVector):
        self.Xvector = XVector
        self.Yvector = YVector
        self.vector =  {self.Xvector: self.Yvector}
        self.magnitude = self.get_magnitude()
        self.unitVector=self.unit_vector()


    def get_magnitude(self):
        for coordinate, coordinate1 in self.vector.items():
            self.exponentDict[coordinate ** 2] = coordinate1 ** 2
        for exponent1, exponent2 in self.exponentDict.items():
            answer = math.sqrt(exponent1 + exponent2)
        return answer
    def unit_vector(self):
        for x, y in self.vector.items():
            answer = self.unitVector[str((1/self.magnitude) * x)] = (1/self.magnitude) * y
            print((1/self.magnitude) * x)
            print((1/self.magnitude) * y)
        return answer

                     
            
v1 = Vector(2,3)
print(v1.magnitude)
print(v1.unitVector)
