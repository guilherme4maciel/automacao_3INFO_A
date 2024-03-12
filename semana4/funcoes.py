'''

As funções permite modularizar o código, dividir ele em partes
menores que podem ser reaproveitadas. Isso simplifica a codificação.


Estrutura função em python

def nome_funcao(param1, param2, paramN):
    //algum código que a função faz
    return valor_retornado

'''

#cria uma função que calcula a área do triângulo
def CalculateTriangleArea(altura, base):
    area = (base * altura) / 2
    return area

#cria uma função que calcula a área do quadrado
def CalculateSquareArea(lado):
    area = lado * lado
    return area

'''

#Exemplo 1: Chamar a função
area1 = CalculateTriangleArea(100, 10)
print("A área do triângulo 1 é", area1)

#Exemplo 2: Chamar a função novamente
base = float(input('Digite a base: '))
altura = float(input('Digita a altura: '))

area2 = CalculateTriangleArea(base, altura)
print("A área do triângulo 2 é ", area2)

'''