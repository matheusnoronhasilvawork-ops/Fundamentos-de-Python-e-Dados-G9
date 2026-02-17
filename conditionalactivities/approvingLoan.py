'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas 
condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.

Crie um programa que receba como entrada a renda mensal de Pedro e 
o valor da parcela desejada. O programa deve informar se o empréstimo 
foi aprovado ou negado com base nas condições acima.
'''

from rich import print

monthly_income = int(input('Enter your monthly income: '))
installment_desired = int(input('Enter the desired installment amount: '))

percentage_installment = (installment_desired / monthly_income) * 100

if monthly_income > 2000 and percentage_installment <= 30:
    print(
        f'[bold green]Loan Approved[/bold green] \n' 
        f'monthly income: {monthly_income} \n' 
        f'percentage of installment: {percentage_installment:.2f}%')
else:
    print(
        f'[bold red]Loan denied[/bold red] \n'
        f'monthly income: {monthly_income} \n'
        f'percentage of installment: {percentage_installment:.2f}%'
        )
