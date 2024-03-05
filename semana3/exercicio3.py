'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''
dia =[]
tarde = []
noite = []

while True: 
    matricula = int(input("Digite o número de matricula: (0 para parar!)"))

    if matricula == 0:
        break
    
    if matricula % 3 == 0:
       dia.append(matricula)
   
    elif matricula % 3 == 1:
        tarde.append(matricula)
    
    else:
        noite.append(matricula)

        print("Alunos da manha", dia)
        print("Alunos da tarde", tarde)
        print("Alunos da noite", noite)
