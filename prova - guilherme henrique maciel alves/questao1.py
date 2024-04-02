'''Cássia precisa de ajuda para calcular a quantidade de gotas de
medicamento para sua filha. Construa um programa que solicite a
concentração de princípio ativo do medicamento em mg/ml, o peso da
criança e a dose recomendada em mg por kg. O programa deve calcular a
dose total multiplicando o peso da criança pela dose por kg recomendada
e dividindo pelo conteúdo do medicamento em mg por ml. Para obter a
quantidade de gotas, multiplica-se o resultado por 20, já que 1 ml equivale
a aproximadamente 20 gotas.'''

concen_medicamento = int(input("Informe a concentração do medicamento(mg/ml): "))

peso = int(input("Informe o peso da criança(kg): "))

dose_recomendada = int(input("Informe a dose recomendada para criança(mg/kg): "))

dose_total = (peso * dose_recomendada)/concen_medicamento

qtd_gotas = int(dose_total * 20)

print("Quantidade de gotas é: ",qtd_gotas)
                       
    