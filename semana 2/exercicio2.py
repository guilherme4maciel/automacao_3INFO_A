'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''

nota = int(input("Digite a nota do aluno: "))
frequen = int(input("Digite o nivel de frequencia do aluno:"))

if nota < 6 or frequen < 75:
    print("Este aluno esta reprovado!")
else:
    print("Este aluno esta aprovado")