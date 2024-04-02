'''Crie um programa que calcule o valor total das compras de um cliente. O
programa deve solicitar indefinidamente que o usuário digite o preço de
cada produto adquirido. Quando o usuário digitar a tecla 'igual' no lugar
do preço do produto, o programa deve exibir a soma dos preços de todos
os produtos digitados'''


while True:

    preco = (input("Digite o preço do produto: "))

    if preco == '=':
        soma = float(preco + 0)
        valor_total = float(0 + preco)
        print(valor_total)
        break       

