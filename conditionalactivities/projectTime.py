'''
Camila está organizando um projeto e precisa calcular o tempo total 
necessário para concluir três atividades: A, B e C. No entanto, se alguma 
atividade tiver um número de dias negativo, o código deve avisar que os 
valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e 
exiba o tempo total do projeto. Se algum valor for negativo, mostre uma 
mensagem informando o erro.
'''


days_for_activityA = int(input("Informe os dias para a atividade A: "))
days_for_activityB = int(input("Informe os dias para a atividade B: "))
days_for_activityC = int(input("Informe os dias para a atividade C: "))

if days_for_activityA < 0 or days_for_activityB < 0 or days_for_activityC < 0:
    print("Os dias não podem ser negativos.")
elif days_for_activityA == "" or days_for_activityB == "" or days_for_activityC == "":
    print("Os dias não podem ser vazios.")
else:
    print(days_for_activityA + days_for_activityB + days_for_activityC)
    
