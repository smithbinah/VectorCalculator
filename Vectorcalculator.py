import math
class Vector:
    exponentArray = []
    def __init__(self, XVector, YVector):
        self.Xvector = XVector
        self.Yvector = YVector
        self.vector =  [self.Xvector, self.Yvector]

    def magnitude(self):
        for coordinate in self.vector:
            self.exponentArray.append(coordinate ** 2)
v1 = Vector(2,3)
# print(v1.vector)
v1.magnitude()
print(v1.exponentArray)

