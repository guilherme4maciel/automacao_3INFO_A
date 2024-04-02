'''Crie um programa que recebe como entrada um número inteiro. Caso o
número digitado seja negativo, o programa deve imprimir ‘Retroceder’; se
o número for 0, imprimir ‘Pare’; e se for um número positivo, imprimir
‘Avançar’.'''



while True: 
    numero = int(input("Digite um número: "))
    
    if numero < 0: 
        print("Retroceder")
    
    if numero > 0:
        print("Avançar")


    if numero == 0:
        print("Pare!")   
        break        