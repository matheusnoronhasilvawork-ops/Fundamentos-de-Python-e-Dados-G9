'''
Uma professora precisa de um programa que ajude a calcular a média 
final dos alunos e informe se foram aprovados, ficaram de recuperação 
ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado

Escreva um programa que receba três notas como entrada e calcule a 
média final. Com base na média, exiba a situação do aluno.
'''

grade1 = float(input("Enter you first grade: "))
grade2 = float(input("Enter you second grade: "))
grade3 = float(input("Enter you third grade: "))

average = (grade1 + grade2 + grade3) / 3

if average >= 7:
    print("Approved")
    print(f'{average:.2f}')
elif 5 <= average < 7:
    print("Recovery")
    print(f'{average:.2f}')
else:
    print("Failed")
    print(f'{average:.2f}')