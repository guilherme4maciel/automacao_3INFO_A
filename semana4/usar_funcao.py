#from(do arquivo) funcoes import (importa a função) CalculateTriangleArea
from funcoes import CalculateTriangleArea, CalculateSquareArea


area = CalculateTriangleArea(10, 10)
print('Área: ', area)

areaQuadrado = CalculateSquareArea(10)
print('Área do quadrado', areaQuadrado)